import jsonschema
import yaml

from sync.build_vault import merge, render_note
from sync.facts import check_facts, load_schema, parse_facts
from tests.sync.factories import asset_facts, insight_facts


def checked(data):
    return check_facts(parse_facts(data, data["service"]), None)


def split_note(text):
    _, frontmatter, body = text.split("---\n", 2)
    return yaml.safe_load(frontmatter), body


def test_shared_node_is_merged_across_facts_files():
    nodes, problems = merge([checked(insight_facts()), checked(asset_facts())])
    event = nodes["evt.asset.asset-created"]
    assert problems == []
    assert event.sources == {"asset", "insight"}
    assert [edge["type"] for edge in event.edges] == ["HAS_FIELD"]
    assert {edge["type"] for edge in nodes["svc.insight"].edges} == {"CONSUMES", "WRITES"}


def test_conflicting_property_keeps_first_service_and_warns():
    insight, asset = insight_facts(), asset_facts()
    # bus is not part of the id, so both files stay valid while disagreeing about it
    insight["nodes"][1]["bus"] = "insight-bus"
    asset["nodes"][1]["bus"] = "default"
    nodes, problems = merge([checked(insight), checked(asset)])
    assert nodes["evt.asset.asset-created"].properties["bus"] == "default"
    assert len(problems) == 1
    assert problems[0].severity == "warning"
    assert "bus" in problems[0].message


def test_generated_at_is_newest_extraction_of_its_sources():
    nodes, _ = merge([checked(insight_facts()), checked(asset_facts())])
    assert nodes["evt.asset.asset-created"].generated_at == "2026-09-28T16:00:00Z"
    assert nodes["svc.asset"].generated_at == "2026-09-28T15:00:00Z"


def test_identical_edges_are_deduplicated():
    insight = insight_facts()
    insight["edges"].append(dict(insight["edges"][0]))
    nodes, _ = merge([checked(insight)])
    assert len(nodes["svc.insight"].edges) == 2


def test_rendered_note_frontmatter_and_body():
    nodes, _ = merge([checked(insight_facts()), checked(asset_facts())])
    frontmatter, body = split_note(render_note(nodes["svc.insight"]))
    assert list(frontmatter) == ["id", "type", "name", "path", "generated_at", "contract_version", "sources", "edges"]
    assert frontmatter["contract_version"] == "0.2"
    assert frontmatter["generated_at"] == "2026-09-28T16:00:00Z"
    assert frontmatter["edges"][0] == {
        "type": "CONSUMES", "to": "evt.asset.asset-created",
        "evidence": "Unite/services/insight/serverless.yml:8", "confidence": 1.0,
        "via": "serverless.yml", "filter": {"record.sourceType": ["RESOURCE_MANAGER"]},
    }
    assert body == (
        "# insight\n\n## Summary\nGenerates insights.\n\n## Links\n"
        "- CONSUMES [[evt.asset.asset-created]]\n- WRITES [[tbl.dynamodb.insight-entities]]\n"
    )


def test_rendered_notes_match_the_vault_note_schema():
    nodes, _ = merge([checked(insight_facts()), checked(asset_facts())])
    validator = jsonschema.Draft202012Validator(load_schema("vault-note.schema.json"))
    for node in nodes.values():
        frontmatter, _ = split_note(render_note(node))
        assert list(validator.iter_errors(frontmatter)) == [], node.id


def test_note_without_edges_says_so():
    nodes, _ = merge([checked(insight_facts())])
    _, body = split_note(render_note(nodes["tbl.dynamodb.insight-entities"]))
    assert body.endswith("## Links\n_No outgoing links._\n")


def test_render_is_deterministic_regardless_of_input_order():
    first, _ = merge([checked(insight_facts()), checked(asset_facts())])
    second, _ = merge([checked(asset_facts()), checked(insight_facts())])
    assert {k: render_note(v) for k, v in first.items()} == {k: render_note(v) for k, v in second.items()}

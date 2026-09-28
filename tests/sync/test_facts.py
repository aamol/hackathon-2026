import pytest

from sync.facts import FactsError, check_facts, load_facts, main, parse_facts
from tests.sync.factories import insight_facts


def messages(checked) -> str:
    return "\n".join(str(problem) for problem in checked.problems)


def test_load_valid_facts(write_facts):
    facts = load_facts(write_facts(insight_facts()))
    assert facts.service == "insight"
    assert len(facts.nodes) == 3
    assert len(facts.edges) == 2


def test_load_rejects_schema_error(write_facts):
    data = insight_facts()
    del data["source_commit"]
    with pytest.raises(FactsError, match="source_commit"):
        load_facts(write_facts(data))


def test_load_rejects_unreadable_file(tmp_path):
    path = tmp_path / "insight.json"
    path.write_text("{ not json")
    with pytest.raises(FactsError, match="cannot read"):
        load_facts(path)


def test_load_rejects_file_name_that_is_not_the_service(write_facts):
    with pytest.raises(FactsError, match="insight.json"):
        load_facts(write_facts(insight_facts(), file_name="asset.json"))


def test_parse_rejects_builder_owned_keys_on_nodes():
    data = insight_facts()
    data["nodes"][0]["edges"] = []
    with pytest.raises(FactsError, match=r"\$\.nodes\[0\]"):
        parse_facts(data, "test")


def test_valid_facts_have_no_problems(fake_unite):
    checked = check_facts(parse_facts(insight_facts(), "test"), fake_unite)
    assert checked.problems == ()
    assert len(checked.nodes) == 3
    assert len(checked.edges) == 2


def test_edge_from_a_node_the_service_does_not_own(fake_unite):
    data = insight_facts()
    data["nodes"].append({"id": "fld.asset.asset-created.asset-id", "type": "field", "name": "assetId",
                          "owner": "evt.asset.asset-created", "data_type": "string"})
    data["edges"].append({"from": "evt.asset.asset-created", "type": "HAS_FIELD",
                          "to": "fld.asset.asset-created.asset-id",
                          "evidence": "Unite/services/insight/serverless.yml:8", "snippet": "- service.asset",
                          "confidence": 1.0, "via": "serverless.yml"})
    checked = check_facts(parse_facts(data, "test"), fake_unite)
    assert "not owned" in messages(checked)
    assert len(checked.edges) == 2


def test_edge_type_not_allowed_between_node_types(fake_unite):
    data = insight_facts()
    data["edges"][1]["type"] = "CONSUMES"  # service CONSUMES table is invalid
    assert "not allowed from service to table" in messages(check_facts(parse_facts(data, "test"), fake_unite))


def test_edge_to_undeclared_node(fake_unite):
    data = insight_facts()
    data["edges"][0]["to"] = "evt.asset.asset-deleted"
    assert "'evt.asset.asset-deleted' is not declared" in messages(check_facts(parse_facts(data, "test"), fake_unite))


def test_filter_only_allowed_on_consumes(fake_unite):
    data = insight_facts()
    data["edges"][1]["filter"] = {"x": ["y"]}
    assert "filter is only allowed on CONSUMES" in messages(check_facts(parse_facts(data, "test"), fake_unite))


@pytest.mark.parametrize(
    "evidence, snippet, expected",
    [
        ("Unite/packages/insight-core/src/repo.ts:2", "PublishCommand", "not found on line 2"),
        ("Unite/packages/insight-core/src/repo.ts:99", "new PutCommand", "past end of file"),
        ("Unite/packages/insight-core/src/missing.ts:1", "new PutCommand", "does not exist"),
        ("Unite/../secret.txt:1", "new PutCommand", "escapes the Unite checkout"),
    ],
)
def test_evidence_problems(fake_unite, evidence, snippet, expected):
    data = insight_facts()
    data["edges"][1]["evidence"] = evidence
    data["edges"][1]["snippet"] = snippet
    checked = check_facts(parse_facts(data, "test"), fake_unite)
    assert expected in messages(checked)
    assert [edge["type"] for edge in checked.edges] == ["CONSUMES"]


def test_evidence_check_skipped_without_unite_root():
    data = insight_facts()
    data["edges"][1]["snippet"] = "PublishCommand"
    assert check_facts(parse_facts(data, "test"), None).problems == ()


def test_node_missing_type_specific_property_is_dropped_with_its_edges(fake_unite):
    data = insight_facts()
    del data["nodes"][2]["physical_name"]
    text = messages(check_facts(parse_facts(data, "test"), fake_unite))
    assert "physical_name" in text
    assert "'tbl.dynamodb.insight-entities' is not declared" in text


def test_node_id_prefix_must_match_type(fake_unite):
    data = insight_facts()
    data["nodes"][1]["type"] = "queue"
    data["nodes"][1]["physical_name"] = "x"
    assert "does not match type 'queue'" in messages(check_facts(parse_facts(data, "test"), fake_unite))


def test_duplicate_node_in_one_file(fake_unite):
    data = insight_facts()
    data["nodes"].append(dict(data["nodes"][1]))
    assert "declared twice" in messages(check_facts(parse_facts(data, "test"), fake_unite))


def test_cli_exit_codes(write_facts, fake_unite, tmp_path):
    assert main([str(write_facts(insight_facts())), "--unite", str(fake_unite)]) == 0
    broken = insight_facts()
    broken["edges"][1]["snippet"] = "PublishCommand"
    assert main([str(write_facts(broken)), "--unite", str(fake_unite)]) == 1
    unreadable = tmp_path / "insight.json"
    unreadable.write_text("{")
    assert main([str(unreadable), "--unite", str(fake_unite)]) == 2

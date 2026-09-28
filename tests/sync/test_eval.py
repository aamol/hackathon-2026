import json

import pytest

from sync.eval import (Score, agreement, load_ground_truth, main, previous_facts_edges, render_eval,
                       restrict_to_labelled_sources, score)
from tests.sync.factories import commit_all, init_git_repo, insight_facts

A = ("svc.insight", "CONSUMES", "evt.asset.asset-created")
B = ("svc.insight", "WRITES", "tbl.dynamodb.insight-entities")
C = ("svc.insight", "READS", "tbl.dynamodb.insight-entities")


def test_score_per_type_and_overall():
    scores = score(predicted={A, B}, expected={A, C})
    assert scores["ALL"] == Score(true_positives=1, predicted=2, expected=2)
    assert scores["ALL"].precision == 0.5 and scores["ALL"].recall == 0.5
    assert scores["READS"].precision is None and scores["READS"].recall == 0.0
    assert scores["WRITES"].precision == 0.0 and scores["WRITES"].recall is None


def test_unlabelled_sources_do_not_count_as_false_positives():
    other = ("svc.creative", "CALLS", "fn.agentexec.use-agent")
    assert restrict_to_labelled_sources({A, other}, {A}) == {A}


def test_load_ground_truth(tmp_path):
    path = tmp_path / "edges.csv"
    path.write_text("src,type,dst,evidence\nsvc.insight,CONSUMES,evt.asset.asset-created,x:1\n,,,\n")
    assert load_ground_truth(path) == {A}
    path.write_text("from,type,to\n")
    with pytest.raises(ValueError, match="src"):
        load_ground_truth(path)


def test_agreement():
    assert agreement({A, B}, {A, B}) == 1.0
    assert agreement({A, B}, {A, C}) == pytest.approx(1 / 3)
    assert agreement(set(), set()) == 1.0


def test_render_eval_table(tmp_path):
    text = render_eval(score({A, B}, {A, C}), tmp_path / "edges.csv")
    assert "| ALL | 2 | 2 | 1 | 0.50 | 0.50 |" in text
    assert "| READS | 0 | 1 | 0 | – | 0.00 |" in text


def test_previous_facts_edges_from_git(tmp_path):
    repo = tmp_path / "enginav"
    facts = repo / "vault" / "_facts" / "insight.json"
    facts.parent.mkdir(parents=True)
    init_git_repo(repo)
    assert previous_facts_edges(facts) is None  # not committed yet
    facts.write_text(json.dumps(insight_facts()))
    commit_all(repo, "facts")
    assert previous_facts_edges(facts) == {A, B}


def test_cli_diff_lists_added_and_removed(tmp_path, capsys):
    repo = tmp_path / "enginav"
    facts = repo / "vault" / "_facts" / "insight.json"
    facts.parent.mkdir(parents=True)
    init_git_repo(repo)
    data = insight_facts()
    facts.write_text(json.dumps(data))
    commit_all(repo, "facts")
    data["edges"][1]["type"] = "READS"
    facts.write_text(json.dumps(data))
    assert main(["diff", str(facts)]) == 0
    out = capsys.readouterr().out
    assert "insight: +1 -1 edges (was 2, now 2)" in out
    assert "+ svc.insight READS tbl.dynamodb.insight-entities" in out
    assert "- svc.insight WRITES tbl.dynamodb.insight-entities" in out

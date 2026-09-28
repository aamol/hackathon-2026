import pytest

from sync import ids


@pytest.mark.parametrize(
    "text, expected",
    [
        ("AssetCreated", "asset-created"),
        ("resource.failed", "resource-failed"),
        ("PMHSyncStarted", "pmh-sync-started"),
        ("CREATIVE_VERSION_PMH_SYNC_STARTED", "creative-version-pmh-sync-started"),
        ("v1ReadRoutes", "v1-read-routes"),
        ("  already-kebab  ", "already-kebab"),
        ("a__b..c", "a-b-c"),
    ],
)
def test_slug(text, expected):
    assert ids.slug(text) == expected


@pytest.mark.parametrize("text", ["", "   ", "---", "${}"])
def test_slug_rejects_text_without_letters_or_digits(text):
    with pytest.raises(ValueError):
        ids.slug(text)


@pytest.mark.parametrize(
    "path, expected",
    [
        ("/v1/analytics/{proxy+}", "v1-analytics-proxy"),
        ("/v1/assets/{assetId}", "v1-assets-asset-id"),
        ("/v1/resources", "v1-resources"),
    ],
)
def test_path_slug(path, expected):
    assert ids.path_slug(path) == expected


@pytest.mark.parametrize(
    "name, expected",
    [
        ("insight-${self:custom.T.STAGE}-Entities", "insight-entities"),
        ("${self:custom.T.STAGE}-queue.fifo", "queue"),
        ("event-driver-${sls:stage}", "event-driver"),
        ("plain-name", "plain-name"),
    ],
)
def test_strip_stage(name, expected):
    assert ids.strip_stage(name) == expected


@pytest.mark.parametrize(
    "source, normalized, service",
    [
        ("service.asset.${self:custom.T.STAGE}", "service.asset", "asset"),
        ("service.asset.${process.env.STAGE}", "service.asset", "asset"),
        ("wssbrandx.${self:custom.T.STAGE}", "wssbrandx", "wssbrandx"),
        ("service.resource", "service.resource", "resource"),
    ],
)
def test_event_source_helpers(source, normalized, service):
    assert ids.normalize_source(source) == normalized
    assert ids.source_service(source) == service


def test_id_builders():
    assert ids.service_id("insight") == "svc.insight"
    assert ids.api_id("asset", "GET", "/v1/assets/{id}") == "api.asset.get-v1-assets-id"
    assert ids.event_id("service.asset.${self:custom.T.STAGE}", "AssetCreated") == "evt.asset.asset-created"
    assert ids.event_id("service.resource", "resource.failed") == "evt.resource.resource-failed"
    assert ids.queue_id("insight-${self:custom.T.STAGE}-generation.fifo") == "q.insight-generation"
    assert ids.function_id("agentexec", "useAgent") == "fn.agentexec.use-agent"
    assert ids.table_id("insight-${self:custom.T.STAGE}-Entities") == "tbl.dynamodb.insight-entities"
    assert ids.external_id("@google/genai") == "ext.google-genai"


def test_field_id():
    assert ids.field_id("evt.resource.resource-failed", "createdBy") == "fld.resource.resource-failed.created-by"
    assert ids.field_id("evt.asset.asset-created", "record.sourceType") == "fld.asset.asset-created.record.source-type"
    with pytest.raises(ValueError):
        ids.field_id("svc", "x")


@pytest.mark.parametrize(
    "service, path, expected",
    [
        (
            "asset",
            "Unite/services/asset/src/handlers/create-asset.spec.ts",
            "test.asset.svc-handlers-create-asset-spec",
        ),
        (
            "asset",
            "Unite/services/asset/src/handlers/internal/create-asset.spec.ts",
            "test.asset.svc-handlers-internal-create-asset-spec",
        ),
        (
            "insight",
            "Unite/packages/insight-core/src/eventbridge/asset-created.spec.ts",
            "test.insight.insight-core-eventbridge-asset-created-spec",
        ),
        ("resource", "Unite/packages/filesign/src/utils.spec.ts", "test.resource.filesign-utils-spec"),
        ("resource", "Unite/packages/validator/src/utils.spec.ts", "test.resource.validator-utils-spec"),
        (
            "resource",
            "Unite/services/resource/test/sqs.integration.test.ts",
            "test.resource.unite-services-resource-test-sqs-integration-test",
        ),
    ],
)
def test_test_id_uses_origin_and_path_after_last_src_segment(service, path, expected):
    assert ids.test_id(service, path) == expected


def test_test_id_disambiguates_same_file_name_in_different_directories():
    outer = ids.test_id("asset", "Unite/services/asset/src/handlers/create-asset.spec.ts")
    inner = ids.test_id("asset", "Unite/services/asset/src/handlers/internal/create-asset.spec.ts")
    assert outer != inner


def test_test_id_disambiguates_same_path_in_different_packages():
    filesign = ids.test_id("resource", "Unite/packages/filesign/src/utils.spec.ts")
    validator = ids.test_id("resource", "Unite/packages/validator/src/utils.spec.ts")
    service = ids.test_id("resource", "Unite/services/resource/src/utils.spec.ts")
    assert len({filesign, validator, service}) == 3


def test_unresolved_id_is_deterministic_and_short():
    first = ids.unresolved_id("asset", "process.env.PMH_ENDPOINT")
    assert first == ids.unresolved_id("asset", "process.env.PMH_ENDPOINT")
    assert first.startswith("unres.asset.")
    assert len(first.rsplit(".", 1)[1]) == 6
    assert first != ids.unresolved_id("asset", "process.env.OTHER")


def test_type_and_folder_lookup():
    assert ids.type_of("evt.asset.asset-created") == "event"
    assert ids.type_of("q.insight-generation") == "queue"
    assert ids.folder_of("queue") == "queues"
    with pytest.raises(ValueError):
        ids.type_of("zzz.unknown")
    with pytest.raises(ValueError):
        ids.folder_of("nope")


def test_cli_prints_id(capsys):
    assert ids.main(["event", "service.asset.${self:custom.T.STAGE}", "AssetCreated"]) == 0
    assert capsys.readouterr().out == "evt.asset.asset-created\n"


@pytest.mark.parametrize("argv", [[], ["nope"], ["field", "only-one-arg"], ["service", ""]])
def test_cli_rejects_bad_input(argv):
    assert ids.main(argv) == 2

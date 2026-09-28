"""Id and slug rules from contract v0.2 §3.1. The only place ids are built."""
from __future__ import annotations

import hashlib
import re
import sys

NODE_TYPES: dict[str, tuple[str, str]] = {
    # node type: (id prefix, vault folder)
    "service": ("svc", "services"),
    "api": ("api", "apis"),
    "event": ("evt", "events"),
    "queue": ("q", "queues"),
    "function": ("fn", "functions"),
    "table": ("tbl", "tables"),
    "field": ("fld", "fields"),
    "test": ("test", "tests"),
    "external": ("ext", "externals"),
    "unresolved": ("unres", "unresolved"),
}
PREFIX_TO_TYPE: dict[str, str] = {prefix: node_type for node_type, (prefix, _) in NODE_TYPES.items()}

_CAMEL_BOUNDARY = re.compile(r"([a-z0-9])([A-Z])")
_ACRONYM_BOUNDARY = re.compile(r"([A-Z]+)([A-Z][a-z])")
_NON_ALPHANUMERIC = re.compile(r"[^A-Za-z0-9]+")
_STAGE_PLACEHOLDER = re.compile(r"\$\{[^}]*stage[^}]*\}", re.IGNORECASE)
_SOURCE_FILE_EXTENSION = re.compile(r"\.(ts|tsx|js|mjs|cjs)$")
_SRC_SEGMENT_MARKER = "/src/"
_FIFO_SUFFIX = ".fifo"
_SERVICE_SOURCE_PREFIX = "service."
_UNRESOLVED_HASH_LENGTH = 6


def slug(text: str) -> str:
    split = _ACRONYM_BOUNDARY.sub(r"\1-\2", _CAMEL_BOUNDARY.sub(r"\1-\2", text))
    result = _NON_ALPHANUMERIC.sub("-", split).strip("-").lower()
    if not result:
        raise ValueError(f"cannot build a slug from {text!r}")
    return result


def path_slug(path: str) -> str:
    return slug(path.replace("{", "").replace("}", "").replace("+", ""))


def strip_stage(name: str) -> str:
    without_stage = _STAGE_PLACEHOLDER.sub("", name)
    if without_stage.endswith(_FIFO_SUFFIX):
        without_stage = without_stage[: -len(_FIFO_SUFFIX)]
    return slug(without_stage)


def normalize_source(source: str) -> str:
    return _STAGE_PLACEHOLDER.sub("", source).strip(".")


def source_service(source: str) -> str:
    name = normalize_source(source)
    if name.startswith(_SERVICE_SOURCE_PREFIX):
        name = name[len(_SERVICE_SOURCE_PREFIX):]
    return slug(name)


def service_id(service: str) -> str:
    return f"svc.{slug(service)}"


def api_id(service: str, method: str, path: str) -> str:
    return f"api.{slug(service)}.{slug(method)}-{path_slug(path)}"


def event_id(source: str, detail_type: str) -> str:
    return f"evt.{source_service(source)}.{slug(detail_type)}"


def queue_id(physical_name: str) -> str:
    return f"q.{strip_stage(physical_name)}"


def function_id(service: str, function_key: str) -> str:
    return f"fn.{slug(service)}.{slug(function_key)}"


def table_id(physical_name: str) -> str:
    return f"tbl.dynamodb.{strip_stage(physical_name)}"


def field_id(owner_id: str, field_path: str) -> str:
    if "." not in owner_id:
        raise ValueError(f"owner id must contain a prefix: {owner_id!r}")
    owner_without_prefix = owner_id.split(".", 1)[1]
    path = ".".join(slug(part) for part in field_path.split("."))
    return f"fld.{owner_without_prefix}.{path}"


def test_id(service: str, file_path: str) -> str:
    src_index = file_path.rfind(_SRC_SEGMENT_MARKER)
    relative_path = file_path[src_index + len(_SRC_SEGMENT_MARKER):] if src_index != -1 else file_path
    relative_path = _SOURCE_FILE_EXTENSION.sub("", relative_path)
    return f"test.{slug(service)}.{slug(relative_path)}"


def external_id(name: str) -> str:
    return f"ext.{slug(name)}"


def unresolved_id(service: str, raw: str) -> str:
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:_UNRESOLVED_HASH_LENGTH]
    return f"unres.{slug(service)}.{digest}"


def type_of(node_id: str) -> str:
    prefix = node_id.split(".", 1)[0]
    if prefix not in PREFIX_TO_TYPE:
        raise ValueError(f"unknown id prefix in {node_id!r}")
    return PREFIX_TO_TYPE[prefix]


def folder_of(node_type: str) -> str:
    if node_type not in NODE_TYPES:
        raise ValueError(f"unknown node type {node_type!r}")
    return NODE_TYPES[node_type][1]


BUILDERS = {
    "service": service_id,
    "api": api_id,
    "event": event_id,
    "queue": queue_id,
    "function": function_id,
    "table": table_id,
    "field": field_id,
    "test": test_id,
    "external": external_id,
    "unresolved": unresolved_id,
}
USAGE = """usage: python -m sync.ids <kind> <args...>
  service <service>                 api <service> <METHOD> <path>
  event <source> <detail-type>      queue <physical-name>
  function <service> <function-key> table <physical-name>
  field <owner-id> <field.path>     test <service> <file-path>
  external <name>                   unresolved <service> <raw-expression>"""


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args or args[0] not in BUILDERS:
        print(USAGE, file=sys.stderr)
        return 2
    try:
        print(BUILDERS[args[0]](*args[1:]))
    except (TypeError, ValueError) as error:
        print(f"error: {error}\n{USAGE}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

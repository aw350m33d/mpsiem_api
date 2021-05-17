from enum import Enum


_TEMPLATE_DIRECTORY = "..\\..\\jinja_templates"


class LimitSettings:

    limit_ptkb_objects = 1000
    limit_tabular_rows = 2000
    limit_deploy_logs = 50
    limit_macros = 100
    limit_events = 100
    limit_incidents = 50
    limit_threads = 4


class SIEMSettings:
    """SIEMOptions Стандартные порты SIEM"""

    PTKB_PORT = 8091
    CORE_PORT = 3334


class AUTHParams(Enum):
    """AUTHParams Параметры аутентификации в MPSIEM"""

    LOCAL = 0
    LDAP = 1



class JinjaSettings:

    template_directory_path = _TEMPLATE_DIRECTORY


class EventAutoComplite:

    values = [
        "msgid",
        "detect",
        "event_src.host",
        "event_src.hostname",
        "event_src.ip",
        "event_src.fqdn",
        "contains",
        "correlation_name",
        "src.ip",
        "src.host",
        "src.hostname",
        "src.port",
        "protocol",
        "direction",
        "dst.port",
        "dst.ip",
        "dst.host",
        "dst.hostname",
        "datafield1",
        "datafield2",
        "datafield3",
        "datafield4",
        "datafield5",
        "datafield6",
        "datafield7",
        "datafield8",
        "datafield9",
        "datafield10",
        "object.name",
        "object.path",
        "object.value",
        "object.id",
        "object.version",
        "importance",
        "subject.name",
        "subject.id",
        "subject.domain",
        "and",
        "or",
        "match",
        "body",
        "assigned_src_ip",
        "event_src.title",
        "event_src.vendor",
        "object.hash",
        "object.property",
        "correlation_name",
        "correlation_type",
        "action",
        "object",
        "status",
        "reason",
        "category.low",
        "category.generic",
        "category.high",
        "uuid",
        "id",
        "in_subnet",
        "logon_type",
    ]

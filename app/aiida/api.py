from config import GLOBAL_CONFIG, api
from .resource import (
    CalcJobNode,
    Computer,
    Group,
    Node,
    ProcessNode,
    QueryBuilder,
    ServerInfo,
    User,
)

prefix = "/aiida"
posting = GLOBAL_CONFIG.get("CLI_DEFAULTS", {}).get("posting", False)

api.add_resource(
    ServerInfo,
    prefix + "/server/",
    prefix + "/server/endpoints/",
    endpoint="server",
    strict_slashes=False,
)

if posting:
    api.add_resource(
        QueryBuilder,
        prefix + "/querybuilder/",
        endpoint="querybuilder",
        strict_slashes=False,
    )

## Add resources and endpoints to the api
api.add_resource(
    Computer,
    # supported urls
    prefix + "/computers/",
    prefix + "/computers/page/",
    prefix + "/computers/page/<int:page>/",
    prefix + "/computers/<id>/",
    prefix + "/computers/projectable_properties/",
    endpoint="computers",
    strict_slashes=False,
)

api.add_resource(
    Node,
    prefix + "/nodes/",
    prefix + "/nodes/projectable_properties/",
    prefix + "/nodes/statistics/",
    prefix + "/nodes/full_types/",
    prefix + "/nodes/full_types_count/",
    prefix + "/nodes/download_formats/",
    prefix + "/nodes/page/",
    prefix + "/nodes/page/<int:page>/",
    prefix + "/nodes/<id>/",
    prefix + "/nodes/<id>/links/incoming/",
    prefix + "/nodes/<id>/links/incoming/page/",
    prefix + "/nodes/<id>/links/incoming/page/<int:page>/",
    prefix + "/nodes/<id>/links/outgoing/",
    prefix + "/nodes/<id>/links/outgoing/page/",
    prefix + "/nodes/<id>/links/outgoing/page/<int:page>/",
    prefix + "/nodes/<id>/links/tree/",
    prefix + "/nodes/<id>/contents/attributes/",
    prefix + "/nodes/<id>/contents/extras/",
    prefix + "/nodes/<id>/contents/derived_properties/",
    prefix + "/nodes/<id>/contents/comments/",
    prefix + "/nodes/<id>/repo/list/",
    prefix + "/nodes/<id>/repo/contents/",
    prefix + "/nodes/<id>/download/",
    endpoint="nodes",
    strict_slashes=False,
)

api.add_resource(
    ProcessNode,
    prefix + "/processes/projectable_properties/",
    prefix + "/processes/<id>/report/",
    endpoint="processes",
    strict_slashes=False,
)

api.add_resource(
    CalcJobNode,
    prefix + "/calcjobs/<id>/input_files/",
    prefix + "/calcjobs/<id>/output_files/",
    endpoint="calcjobs",
    strict_slashes=False,
)

api.add_resource(
    User,
    prefix + "/users/",
    prefix + "/users/projectable_properties/",
    prefix + "/users/page/",
    prefix + "/users/page/<int:page>/",
    prefix + "/users/<id>/",
    endpoint="users",
    strict_slashes=False,
)

api.add_resource(
    Group,
    prefix + "/groups/",
    prefix + "/groups/projectable_properties/",
    prefix + "/groups/page/",
    prefix + "/groups/page/<int:page>/",
    prefix + "/groups/<id>/",
    endpoint="groups",
    strict_slashes=False,
)

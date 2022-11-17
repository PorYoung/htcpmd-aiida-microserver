from flask import request
from common.BaseResource import BaseResource
from common.utils import Utils, list_routes


class EndPointsResource(BaseResource):
    def get(self):
        data = dict(
            method=request.method,
            url=self.url,
            url_root=self.url_root,
            path=self.path,
            query_string=self.query_string,
            resource_type="Info",
            available_endpoints=list_routes(),
        )

        return Utils.build_response(data=data)

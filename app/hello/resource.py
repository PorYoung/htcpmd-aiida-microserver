from datetime import datetime
import flask
from flask_restful import Resource
from common.BaseResource import BaseResource
from common.utils import Utils


class Hello(BaseResource):
    def get(self, id):
        return Utils.build_response(
            data={"id": id, "datetime": datetime.now().isoformat()}
        )

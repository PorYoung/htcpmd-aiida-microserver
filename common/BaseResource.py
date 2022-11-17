from flask import request
from flask_restful import Resource
from urllib.parse import unquote
from common.utils import Utils
from config import GLOBAL_CONFIG


class BaseResource(Resource):
    path = None
    url = None
    url_root = None
    query_string = None

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.utils = Utils(**GLOBAL_CONFIG.get("API_CONFIG"))

        self.path = unquote(request.path)
        self.url = unquote(request.url)
        self.url_root = unquote(request.url_root)
        self.query_string = unquote(request.query_string.decode("utf-8"))

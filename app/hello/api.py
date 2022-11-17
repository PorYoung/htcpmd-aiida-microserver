from config import api
from .resource import Hello

api.add_resource(Hello, "/hello", "/hello/<string:id>")

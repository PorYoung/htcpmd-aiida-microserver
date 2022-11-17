import app
from config import api
from .resource import EndPointsResource

api.add_resource(EndPointsResource, "/", "/endpoints", endpoint="endpoints")

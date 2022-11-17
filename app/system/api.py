import app
from config import api
from .resource import System

api.add_resource(System, "/system", endpoint="system")

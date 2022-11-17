from . import config, nacos
from .app import get_app_instance
from .api import get_api_instance

INSTANCE = config.INSTANCE
GLOBAL_CONFIG = config.GLOBAL_CONFIG
app = get_app_instance()
api = get_api_instance()

__all__ = (INSTANCE, GLOBAL_CONFIG, app, api, nacos)

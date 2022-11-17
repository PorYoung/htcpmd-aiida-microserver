from common.BaseResource import BaseResource
from common.utils import Utils
from config import GLOBAL_CONFIG


class System(BaseResource):
    def get(self):
        print(self.path)

        return Utils.build_response(data=GLOBAL_CONFIG)

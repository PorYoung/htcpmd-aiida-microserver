# from .config import NACOS
from common.utils import DotDict
from .config import GLOBAL_CONFIG
import KcangNacos.nacos as nacos

NACOS = DotDict(GLOBAL_CONFIG.get("NACOS"))

nacosServer = nacos.nacos(ip=NACOS.ip, port=NACOS.port)

nacosServer.config(
    dataId=NACOS.data_id,
    myConfig=GLOBAL_CONFIG,
    group=NACOS.group,
    tenant=NACOS.namespace,
)

nacosServer.registerService(
    serviceIp=NACOS.ip,
    servicePort=NACOS.port,
    serviceName=NACOS.server_name,
    namespaceId=NACOS.namespace,
    groupName=NACOS.group,
)

nacosServer.healthyCheck()

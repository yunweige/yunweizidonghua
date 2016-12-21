from services import linux

class BaseTemplate:
    name = None
    service = None
    hostname = None
    ip_address = None
    port = None
    os = None

class LinuxGeneralServices(BaseTemplate):
    name = 'Linux General Services'
    services = {
        'cpu': linux.cpu(),
        'memory': linux.memory,
        'load': linux.load(),
    }

class WindowsGeneralService(BaseTemplate):
    name = 'Windows General Services'
    #groups = ['BJ']
    hosts = ['localhost','www.baidu.com']
    services = {
        'load': linux.load(),
        'memory':  linux.memory(),
        'cpu': linux.cpu(),
    }
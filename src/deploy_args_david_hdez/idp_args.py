from abc import ABC
from abc import abstractmethod


class ProgramArgs(ABC):
    def __init__(self):
        self._region = None
        self._team = None
        self._project = None
        self._owner = None
        self._service_name = None

    @property
    def region(self):
        return self._region

    @property
    def team(self):
        return self._team

    @property
    def project(self):
        return self._project

    @property
    def owner(self):
        return self._owner

    @property
    def service_name(self):
        return self._service_name

    @region.setter
    def region(self, value: str):
        self._region = value

    @team.setter
    def team(self, value: str):
        self._team = value

    @project.setter
    def project(self, value: str):
        self._project = value

    @owner.setter
    def owner(self, value: str):
        self._owner = value

    @service_name.setter
    def service_name(self, value: str):
        self._service_name = value

    @abstractmethod
    def process_payload(self, payload: dict):
        pass


class ExecuteStopFuncArgs(ProgramArgs):
    def __init__(self):
        super().__init__()
        self.tags = None
        self.cron_expr = None

    def process_payload(self, payload: dict):
        for key in ('tags', 'cron_expr'):
            if key in payload.keys():
                setattr(self, key, payload[key])


class DbManagedArgs(ProgramArgs):
    def __init__(self):
        super().__init__()
        self.name = None
        self.engine = None
        self.instance_class = None
        self.username = None
        self.password = None
        self.storage = None
        self.st_type = None
        self.is_public = None
        self.db_name = None
        self.store_creds = None
        self.secret_kms_key = None

    def process_payload(self, payload: dict):
        for key in ('engine', 'instance_class', 'storage', 'store_creds',
                    'st_type', 'is_public', 'username', 'secret_kms_key',
                    'password', 'db_name', 'tags'):
            if key in payload.keys():
                setattr(self, key, payload[key])


class VmArgs(ProgramArgs):
    def __init__(self):
        super().__init__()
        self.os = None
        self.cpu = None
        self.storage = None
        self.disk_type = None
        self.instance_type = None
        self.data = None
        self.tags = None
        self.vpc = None
        self.pub_key = None

    def process_payload(self, payload: dict):
        for key in ('os', 'cpu', 'storage',
                    'disk_type', 'vpc', 'pub_key',
                    'data', 'instance_type', 'tags'):
            if key in payload.keys():
                setattr(self, key, payload[key])


class VpcArgs(ProgramArgs):
    def __init__(self):
        super().__init__()
        self.network = None
        self.network_suffix = None
        self.public_subnets = None
        self.private_subnets = None

    def process_payload(self, payload: dict):
        for key in ('network', 'network_suffix', 'public_subnets', 'private_subnets'):
            if key in payload.keys():
                setattr(self, key, payload[key])


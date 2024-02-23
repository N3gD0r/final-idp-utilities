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

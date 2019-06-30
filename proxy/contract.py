from abc import abstractmethod, ABCMeta
from datetime import datetime


class Contract(metaclass=ABCMeta):
    @abstractmethod
    def is_available(self):
        pass

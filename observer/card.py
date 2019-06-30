from abc import ABCMeta, abstractmethod


class Card(metaclass=ABCMeta):
    @abstractmethod
    def update(self, number):
        pass

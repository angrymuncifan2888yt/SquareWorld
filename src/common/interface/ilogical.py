from abc import ABC, abstractmethod


class ILogical(ABC):
    @abstractmethod
    def update(self):
        pass

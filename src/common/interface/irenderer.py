from abc import ABC, abstractmethod


class IRenderer(ABC):
    @abstractmethod
    def render(screen, obj, camera):
        pass

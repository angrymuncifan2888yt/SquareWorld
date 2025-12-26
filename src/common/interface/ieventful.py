from abc import ABC, abstractmethod
from common import Event
from typing import List


class IEventful(ABC):
    def __init__(self):
        super().__init__()

        self.entity_events: List[Event] = []

    def emit_event(self, event: Event):
        self.entity_events.append(event)
    
    @abstractmethod
    def handle_event(self, event):
        pass

    def handle_events(self, events: list):
        for event in events:
            self.handle_event(event)

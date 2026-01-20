import pygame

from .ui_object import UiObject


class UiManager:
    def __init__(self):
        self.ui_objects = []

    def add_ui_object(self, obj: UiObject):
        self.ui_objects.append(obj)

    def remove_ui_object(self, obj: UiObject):
        if obj in self.ui_objects:
            self.ui_objects.remove(obj)

    def input(self, delta, pygame_event):
        for obj in self.ui_objects:
            obj.input(delta, pygame_event)

    def update(self, delta_time: float, pygame_event):
        for obj in self.ui_objects:
            obj.update(delta_time, pygame_event)

    def render(self, screen):
        for obj in self.ui_objects:
            obj.render(screen)

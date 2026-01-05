import pygame
from core import Position, Timer
from .text_cursor import TextCursor

class TypingField:
    def __init__(self, position: Position, font=None):
        self.position = position
        self.text: str = ""
        self.active = True
        self.font = font or pygame.font.Font(None, 30)

        self.backspace_timer = Timer(0.05)
        self.text_cursor = TextCursor(self.position)

    def type(self, pg_events, delta: float):
        self.text_cursor.update(delta)
        keys = pygame.key.get_pressed()
        command = None

        for event in pg_events:
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    command = self.text
                    self.text = ""

                elif event.key == pygame.K_LEFT:
                    if self.text_cursor.current_symbol > 0:
                        self.text_cursor.current_symbol -= 1

                elif event.key == pygame.K_RIGHT:
                    if self.text_cursor.current_symbol < len(self.text):
                        self.text_cursor.current_symbol += 1

                elif event.key == pygame.K_BACKSPACE:
                    if self.text_cursor.current_symbol > 0:
                        self.text = (
                            self.text[:self.text_cursor.current_symbol - 1] +
                            self.text[self.text_cursor.current_symbol:]
                        )
                        self.text_cursor.current_symbol -= 1

                else:
                    if event.key != pygame.K_ESCAPE and event.key != pygame.K_TAB\
                        and event.key != pygame.K_SLASH:
                        self.text = (
                        self.text[:self.text_cursor.current_symbol] +
                        event.unicode +
                        self.text[self.text_cursor.current_symbol:]
                        )
                        self.text_cursor.current_symbol += 1


        if self.active and keys[pygame.K_BACKSPACE]:
            self.backspace_timer.update(delta)
            if self.backspace_timer.finished:
                self.text = self.text[:-1]
                self.backspace_timer.reset()
        else:
            self.backspace_timer.reset()

        # Moving text cursor
        left_text = self.text[:self.text_cursor.current_symbol]
        width = self.font.size(left_text)[0]
        self.text_cursor.position = Position(
            self.position.x + width,
            self.position.y
        )

        # self.text_cursor.position = Position(self.position.x + width, self.position.y)
        return command

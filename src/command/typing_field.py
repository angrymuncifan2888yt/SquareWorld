import pygame
from core import Position, Timer
from .text_cursor import TextCursor

class TypingField:
    def __init__(self, position: Position, font=None):
        # Initialize typing field at a specific position with optional font
        self.position = position
        self.text: str = ""  # Current text in the field
        self.active = True   # Whether typing is active
        self.font = font or pygame.font.Font(None, 30)

        self.backspace_timer = Timer(0.05)  # Timer for continuous backspace
        self.text_cursor = TextCursor(self.position)  # Cursor object
        self.arrow_timer = Timer(0.05)  # Timer for holding left/right arrow keys
        self.arrow_direction = 0        # -1 = left, 1 = right

    def type(self, pg_events, delta: float):
        # Update the text cursor animation
        self.text_cursor.update(delta)
        keys = pygame.key.get_pressed()
        command = None  # Stores the command if Enter is pressed

        # Process events
        for event in pg_events:
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    # Submit command
                    command = self.text
                    self.text = ""

                elif event.key == pygame.K_BACKSPACE:
                    # Delete character before cursor
                    if self.text_cursor.current_symbol > 0:
                        self.text = (
                            self.text[:self.text_cursor.current_symbol - 1] +
                            self.text[self.text_cursor.current_symbol:]
                        )
                        self.text_cursor.current_symbol -= 1

                else:
                    # Add typed character (ignore special keys)
                    if event.key != pygame.K_ESCAPE and event.key != pygame.K_TAB and event.key != pygame.K_SLASH:
                        self.text = (
                            self.text[:self.text_cursor.current_symbol] +
                            event.unicode +
                            self.text[self.text_cursor.current_symbol:]
                        )
                        self.text_cursor.current_symbol += 1

        # Handle holding backspace
        if self.active and keys[pygame.K_BACKSPACE]:
            self.backspace_timer.update(delta)
            if self.backspace_timer.finished:
                self.text = self.text[:-1]
                self.backspace_timer.reset()
        else:
            self.backspace_timer.reset()

        # Handle holding left/right arrow keys
        if self.active:
            if keys[pygame.K_LEFT]:
                self.arrow_timer.update(delta)
                if self.arrow_timer.finished:
                    self.text_cursor.current_symbol = max(0, self.text_cursor.current_symbol - 1)
                    self.arrow_timer.reset()

            if keys[pygame.K_RIGHT]:
                self.arrow_timer.update(delta)
                if self.arrow_timer.finished:
                    self.text_cursor.current_symbol = min(len(self.text), self.text_cursor.current_symbol + 1)
                    self.arrow_timer.reset()

        # Update text cursor position based on text width before cursor
        left_text = self.text[:self.text_cursor.current_symbol]
        width = self.font.size(left_text)[0]
        self.text_cursor.position = Position(
            self.position.x + width,
            self.position.y
        )
        
        return command  # Return command if Enter was pressed

import pygame
import sys
from core import Position
from graphics import HpBar, Text, TempText, Button
from assets import Fonts
from renderer.other import RendererTypingField
from world.nextbot import NextbotKingMunci
from core import Timer
import const
from command import TypingField, execute_command


class HUD:
    def __init__(self, world):
        self.is_on = True  # Flag to show/hide HUD

        # Typing field for commands
        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False  # Whether the player is currently typing a command

        # Player health bar
        self.hp_bar = HpBar(Position(10, 0), world.player.hp)

        # Text fields for debugging
        self.player_pos_text = Text("", Position(10, 10), Fonts.FONT_30)
        self.camera_pos_text = Text("", Position(10, 50), Fonts.FONT_30)
        self.fps_text = Text("", Position(10, 90), Fonts.FONT_30)

        # Text showing Python and Pygame versions
        self.python_pygame_version_text = Text(
            f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}  "
            f"pygame {pygame.version.ver}",
            Position(10, 130),
            Fonts.FONT_30
        )

        # Message for command results or errors, disappears after 5 seconds
        self.command_result_message = TempText(
            "", Position(10, 690), Fonts.FONT_30, color=(200, 0, 0), timer=Timer(5)
        )

        self.chosen_block = None  # Currently selected block

        # King Munci hp bar
        self.boss_hp_bar = HpBar(Position(360, 50), 0, 600, 50, (140, 20, 50), (20, 15, 25), (160, 130, 40))
        self.boss_hp_bar.center_by_x(const.WINDOW_SIZE[0])
        self.show_boss_hp = False

    def update(self, pg_event, delta, world, debug, chosen_block):
        if not self.is_on:
            return

        # Update the temporary command message
        self.command_result_message.update(delta)

        self.chosen_block = chosen_block

        # Update HP bar with current player health
        self.hp_bar.set_max_value(world.player.max_hp)
        self.hp_bar.value = world.player.hp

        # Updating boss bar
        boss = None
        for entity in world.entities:
            if isinstance(entity, NextbotKingMunci):
                boss = entity
                break

        if boss:
            self.show_boss_hp = True
            self.boss_hp_bar.set_max_value(boss.max_hp)
            self.boss_hp_bar.value = boss.hp
        else:
            self.show_boss_hp = False

        # Move HP bar lower if debug info is displayed
        self.hp_bar.position.y = 175 if debug else 50

        # Update player position text
        self.player_pos_text.text = (
            f"x: {round(world.player.position.x, 3)} "
            f"y: {round(world.player.position.y, 3)}"
        )

        # Handle typing commands
        if self.do_type:
            res = self.typing_field.type(pg_event, delta)
            if res:
                result = execute_command(world, res)

                # If command returned an exception, show it in red
                if isinstance(result, Exception):
                    self.command_result_message.color = (200, 0, 0)
                    error_name = result.__class__.__name__
                    error_message = str(result)
                    self.command_result_message.text = f"{error_name}: {error_message}"

                # If command returned a string message, show it in green
                elif isinstance(result, str):
                    self.command_result_message.color = (0, 200, 0)
                    self.command_result_message.text = result

                self.command_result_message.show()  # Display the message

    def render(self, screen, clock, camera, debug):
        if not self.is_on:
            return

        # Render the player's HP bar
        self.hp_bar.render(screen, text=str(self.hp_bar.value))

        # Render boss hp bar if needed
        if self.show_boss_hp:
            self.boss_hp_bar.render(screen, text="King Munci")

        # Render player's position text
        self.player_pos_text.render(screen)

        # Render texture of the currently selected block
        screen.blit(self.chosen_block.texture(), (1090, 10))

        # Render typing field and command result if player is typing
        if self.do_type:
            RendererTypingField.render(screen, self.typing_field, None)
            self.command_result_message.render(screen)

        # Render debug info if enabled
        if debug:
            self.camera_pos_text.text = (
                f"camera.x: {round(camera.position.x, 3)} "
                f"camera.y: {round(camera.position.y, 3)}"
            )
            self.fps_text.text = f"FPS: {round(clock.get_fps(), 3)}"

            self.fps_text.render(screen)
            self.python_pygame_version_text.render(screen)
            self.camera_pos_text.render(screen)

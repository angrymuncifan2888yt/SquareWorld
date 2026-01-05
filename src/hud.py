import pygame
import sys
from core import Position
from graphics import HpBar, Text, TempText
from assets import Fonts
from renderer.graphics import RendererHpBar, RendererText
from renderer.other import RendererTypingField
from core import Timer
from command import TypingField, CommandParser, execute_command


class HUD:
    def __init__(self, world):
        self.is_on = True

        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False

        self.hp_bar = HpBar(Position(10, 0), world.player.hp.hp)
        self.player_pos_text = Text("", Position(10, 10), Fonts.FONT_30)
        self.camera_pos_text = Text("", Position(10, 50), Fonts.FONT_30)
        self.fps_text = Text("", Position(10, 90), Fonts.FONT_30)

        self.python_pygame_version_text = Text(
            f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}  "
            f"pygame {pygame.version.ver}",
            Position(10, 130),
            Fonts.FONT_30
        )
        self.command_result_message = TempText("", Position(10, 690),
                                               Fonts.FONT_30, color=(200, 0, 0), timer=Timer(5))
        self.chosen_block = None

    def update(self, pg_event, delta, world, debug, chosen_block):
        if not self.is_on:
            return

        self.command_result_message.update(delta)
        self.chosen_block = chosen_block
        self.hp_bar.set_max_value(world.player.hp.max_hp)
        self.hp_bar.value = world.player.hp.hp

        self.hp_bar.position.y = 175 if debug else 50

        self.player_pos_text.text = (
            f"x: {round(world.player.position.x, 3)} "
            f"y: {round(world.player.position.y, 3)}"
        )

        if self.do_type:
            res = self.typing_field.type(pg_event, delta)
            if res:
                parsed_cmd = CommandParser.parse(res)
                result = execute_command(world, parsed_cmd)

                if isinstance(result, Exception):
                    self.command_result_message.color = (200, 0, 0)
                    error_name = result.__class__.__name__
                    error_message = str(result)
                    self.command_result_message.text = f"{error_name}: {error_message}"

                
                elif isinstance(result, str):
                    self.command_result_message.color = (0, 200, 0)
                    self.command_result_message.text = result

                self.command_result_message.show()
                # self.do_type = False

    def render(self, screen, clock, camera, debug):
        if not self.is_on:
            return

        RendererHpBar.render(screen, self.hp_bar)
        RendererText.render(screen, self.player_pos_text)
        screen.blit(self.chosen_block.texture(), (1090, 10))

        if self.do_type:
            RendererTypingField.render(screen, self.typing_field, None)
            self.command_result_message.render(screen)

        if debug:
            self.camera_pos_text.text = (
                f"camera.x: {round(camera.position.x, 3)} "
                f"camera.y: {round(camera.position.y, 3)}"
            )
            self.fps_text.text = f"FPS: {round(clock.get_fps(), 3)}"

            RendererText.render(screen, self.fps_text)
            RendererText.render(screen, self.python_pygame_version_text)
            RendererText.render(screen, self.camera_pos_text)

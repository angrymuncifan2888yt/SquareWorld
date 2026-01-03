import pygame
import sys
from core import Position
from graphics import HpBar, Text
from assets import Fonts
from renderer.graphics import RendererHpBar, RendererText
from renderer.other import RendererTypingField
from command import TypingField, CommandParser, execute_command


class HUD:
    def __init__(self, world):
        self.is_on = True

        self.typing_field = TypingField(Position(10, 750), Fonts.FONT_30)
        self.do_type = False

        self.hp_bar = HpBar(Position(10, 0), world.player.hp.hp)
        self.player_pos_text = Text(f"",
                                    Position(10, 10), Fonts.FONT_30)

        self.camera_pos_text = Text(f"",
                                    Position(10, 50), Fonts.FONT_30)
        self.fps_text = Text(f"",
                                    Position(10, 90), Fonts.FONT_30)
        self.python_pygame_version_text = Text(
            f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}  "
            f"pygame {pygame.version.ver}",
            Position(10, 130),
            Fonts.FONT_30
        )

        self.hud = True

    def process_hud(self, screen, clock, camera, pg_event, delta, world, debug):
        if self.hud:
            self.hp_bar.set_max_value(world.player.hp.max_hp)
            self.hp_bar.value = world.player.hp.hp
            if debug:
                self.hp_bar.position.y = 175

            else:
                self.hp_bar.position.y = 50

            self.player_pos_text.text = f"x: {round(world.player.position.x, 3)} y: {round(world.player.position.y, 3)}"

            if self.do_type:
                res = self.typing_field.type(pg_event, delta)

                if res:
                    try:
                        parsed_cmd = CommandParser.parse(res)
                        execute_command(world, parsed_cmd)
                        self.do_type = False

                    except Exception:
                        pass

            RendererHpBar.render(screen, self.hp_bar)
            RendererText.render(screen, self.player_pos_text)

            if self.do_type:
                RendererTypingField.render(screen, self.typing_field, None)

            if debug:
                self.camera_pos_text.text = f"camera.x: {round(camera.position.x, 3)} camera.y: {round(camera.position.y, 3)}"
                self.fps_text.text = f"FPS: {round(clock.get_fps(), 3)}"
                RendererText.render(screen, self.fps_text)
                RendererText.render(screen, self.python_pygame_version_text)
                RendererText.render(screen, self.camera_pos_text)

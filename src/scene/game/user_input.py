import pygame
from world.block import *
from core import Position, Direction
from common import const
from ..scene_list import SceneList
from assets import Sound


def user_input(self, pg_event, delta):
    keys_pressed = pygame.key.get_pressed()

    if not self.hud.do_type:
        if keys_pressed[pygame.K_a]:
            self.world.player.position.move(Direction.LEFT, self.world.player.speed, self.world.delta)

        if keys_pressed[pygame.K_d]:
            self.world.player.position.move(Direction.RIGHT, self.world.player.speed, self.world.delta)

        if keys_pressed[pygame.K_w]:
            self.world.player.position.move(Direction.TOP, self.world.player.speed, self.world.delta)

        if keys_pressed[pygame.K_s]:
            self.world.player.position.move(Direction.DOWN, self.world.player.speed, self.world.delta)

        # Camera movement
        if keys_pressed[pygame.K_j]:  # KJ!!!!!
            self.camera.position.move(Direction.LEFT, const.CAMERA_SPEED, delta)
            self.free_cam = True

        if keys_pressed[pygame.K_l]:
            self.camera.position.move(Direction.RIGHT, const.CAMERA_SPEED, delta)
            self.free_cam = True

        if keys_pressed[pygame.K_i]:
            self.camera.position.move(Direction.TOP, const.CAMERA_SPEED, delta)
            self.free_cam = True

        if keys_pressed[pygame.K_k]:
            self.camera.position.move(Direction.DOWN, const.CAMERA_SPEED, delta)
            self.free_cam = True

    for event in pg_event:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                self.free_cam = False

            elif event.key == pygame.K_F1:
                self.hud.is_on = not self.hud.is_on
            
            elif event.key == pygame.K_TAB:
                self.debug = not self.debug

            elif event.key == pygame.K_SLASH:
                if self.hud.is_on:
                    self.hud.do_type = not self.hud.do_type
                        
            if not self.hud.do_type:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    number = event.key - pygame.K_1  # 1 → 0, 2 → 1

                    if 0 <= number < len(self.blocks):
                        self.current_block_index = number

                elif event.key == pygame.K_RETURN:
                    self.scene_manager.set_scene(SceneList.MAIN_MENU)
                    self.world.stop()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos

                world_x = mouse_x + self.camera.position.x
                world_y = mouse_y + self.camera.position.y

                self.world.add_block(
                    self.blocks[self.current_block_index](
                        self.world,
                        Position(world_x, world_y)
                    )
                )

            elif event.button == 3:
                mouse_x, mouse_y = event.pos

                world_x = mouse_x + self.camera.position.x
                world_y = mouse_y + self.camera.position.y

                for block in self.world.blocks[:]:
                    bx = block.position.x
                    by = block.position.y

                    if bx <= world_x <= bx + block.hitbox.width and by <= world_y <= by + block.hitbox.height:
                        if self.world.player.god_mode:
                            self.world.remove_block(block)
                        block.damage(1)
                        Sound.breaking()
                        break
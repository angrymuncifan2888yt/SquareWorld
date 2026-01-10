import pygame
from world.block import *
from world.block.entity_block import EntityBlock
from core import Position, Direction
import const
from ..scene_list import SceneList
from assets import SoundStorage


def user_input(self, pg_event, delta):
    # Get the state of all pressed keys
    keys_pressed = pygame.key.get_pressed()

    # Player movement (only if not typing a command)
    if not self.hud.do_type:
        if keys_pressed[pygame.K_a]:
            self.world.player.position.move(Direction.LEFT, self.world.player.speed, self.world.delta)
        if keys_pressed[pygame.K_d]:
            self.world.player.position.move(Direction.RIGHT, self.world.player.speed, self.world.delta)
        if keys_pressed[pygame.K_w]:
            self.world.player.position.move(Direction.TOP, self.world.player.speed, self.world.delta)
        if keys_pressed[pygame.K_s]:
            self.world.player.position.move(Direction.DOWN, self.world.player.speed, self.world.delta)

        # Camera movement (free camera mode)
        if keys_pressed[pygame.K_j]:
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

    # Handle key and mouse events
    for event in pg_event:
        if event.type == pygame.KEYDOWN:
            # Reset camera to player if H is pressed
            if event.key == pygame.K_h:
                self.free_cam = False

            # Toggle HUD visibility
            elif event.key == pygame.K_F1:
                self.hud.is_on = not self.hud.is_on

            # Toggle debug mode
            elif event.key == pygame.K_TAB:
                self.debug = not self.debug

            # Toggle typing field for commands
            elif event.key == pygame.K_SLASH:
                if self.hud.is_on:
                    self.hud.do_type = not self.hud.do_type

            # Block selection (keys 1–9) and scene reset
            if not self.hud.do_type:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    number = event.key - pygame.K_1  # Convert key to index 0–8
                    if 0 <= number < len(self.blocks):
                        self.current_block_index = number

                elif event.key == pygame.K_RETURN:
                    # Return to main menu and stop world sounds
                    self.scene_manager.set_scene(SceneList.MAIN_MENU)
                    self.world.stop_sound()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left click → place selected block
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                world_x = mouse_x + self.camera.position.x
                world_y = mouse_y + self.camera.position.y

                self.world.add_entity(
                    self.blocks[self.current_block_index](
                        self.world,
                        Position(world_x, world_y)
                    )
                )

            # Right click → damage or remove block under cursor
            elif event.button == 3:
                mouse_x, mouse_y = event.pos
                world_x = mouse_x + self.camera.position.x
                world_y = mouse_y + self.camera.position.y

                # Iterate through all blocks to find one under the cursor
                for block in self.world.entities[:]:
                    if isinstance(block, EntityBlock):
                        bx = block.position.x
                        by = block.position.y

                        if bx <= world_x <= bx + block.hitbox.width and by <= world_y <= by + block.hitbox.height:
                            if self.world.player.god_mode:
                                # Remove block instantly in god mode
                                self.world.remove_entity(block)
                                SoundStorage.BREAKING.play()
                            else:
                                # Damage block and play breaking sound
                                block.damage(1)
                                SoundStorage.BREAKING.play()
                            break

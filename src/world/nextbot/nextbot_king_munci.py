from .entity_nextbot import EntityNextbot
from .nextbot_asya import NextbotAsya
from .nextbot_angry_munci import NextbotAngryMunci
from assets import SoundStorage, AdvancedSound, Sprites, calculate_sound_volume
from ..components import HasHealth
from ..other import EntityBullet
from core import Timer, Position, Vec2
import math
import random


class NextbotKingMunci(EntityNextbot, HasHealth):
    @classmethod
    def image(cls):
        return Sprites.KING_MUNCI_TEXTURE

    def __init__(self, world, position, creation_params=None):
        super().__init__(
            world,
            position,
            220,
            260,
            AdvancedSound(SoundStorage.ANGRY_MUNCI_AMBIENCE),
            700,
            1,
            creation_params
        )

        self.max_hp = 1000
        self.hp = self.max_hp
        self.block_break_timer = Timer(0.2)
        self.can_damage_block = False

        self.summon_asya_timer = Timer(1.5)
        self.summon_angry_timer = Timer(10.0)  # separate, slower timer for Angry Munci
        self.shoot_timer = Timer(1.5)  # Bullet shooting timer
        self.is_enraged = False
        self.created_entities = []

        self.death_sound = AdvancedSound(SoundStorage.KING_MUNCI_DYING)
        SoundStorage.KING_MUNCI_ROAR.play()

    def update(self, delta):
        super().update(delta)
        self.shoot_timer.update(delta)
        if self.shoot_timer.finished:
            self.shoot_player()
            self.shoot_timer.reset()

        if not self.can_damage_block:
            self.block_break_timer.update(delta)
        if self.block_break_timer.finished:
            self.can_damage_block = True

        if not self.is_enraged and self.hp <= self.max_hp * 0.5:
            self.enter_rage()

        self.summon_asya_timer.update(delta)
        if self.summon_asya_timer.finished:
            self.summon_asya()
            self.summon_asya_timer.reset()

        if self.is_enraged:
            self.summon_angry_timer.update(delta)
            if self.summon_angry_timer.finished:
                self.summon_angry_munci_once()
                self.summon_angry_timer.reset()

    def enter_rage(self):
        self.is_enraged = True
        self.summon_asya_timer.duration = 2.0
        self.speed += 500
        SoundStorage.KING_MUNCI_ROAR.play()

    def shoot_player(self):
        player_pos = self.world.player.position

        dx = player_pos.x - self.position.x
        dy = player_pos.y - self.position.y

        angle = math.degrees(math.atan2(dy, dx))

        direction = Vec2(angle)

        bullet_pos = Position(
            self.position.x + self.hitbox.width // 2,
            self.position.y + self.hitbox.height // 2
        )

        bullet = EntityBullet(
            self.world,
            bullet_pos,
            direction,
            source=self,
            damage=15
        )

        self.world.add_entity(bullet)

    def summon_asya(self):
        player_pos = self.world.player.position
        min_radius = 150
        max_radius = 300
        min_player_distance = 200
        count = random.randint(1, 2)
        for _ in range(count):
            for _ in range(10):
                angle = random.uniform(0, math.tau)
                radius = random.uniform(min_radius, max_radius)
                x = self.position.x + math.cos(angle) * radius
                y = self.position.y + math.sin(angle) * radius
                spawn_pos = Position(x, y)
                dx = spawn_pos.x - player_pos.x
                dy = spawn_pos.y - player_pos.y
                dist_to_player = (dx * dx + dy * dy) ** 0.5
                if dist_to_player >= min_player_distance:
                    entity = NextbotAsya(self.world, spawn_pos)
                    self.created_entities.append(entity)
                    self.world.add_entity(entity)
                    break

    def summon_angry_munci_once(self):
        player_pos = self.world.player.position
        min_radius = 150
        max_radius = 300
        min_player_distance = 200
        for _ in range(10):
            angle = random.uniform(0, math.tau)
            radius = random.uniform(min_radius, max_radius)
            x = self.position.x + math.cos(angle) * radius
            y = self.position.y + math.sin(angle) * radius
            spawn_pos = Position(x, y)
            dx = spawn_pos.x - player_pos.x
            dy = spawn_pos.y - player_pos.y
            dist_to_player = (dx * dx + dy * dy) ** 0.5
            if dist_to_player >= min_player_distance:
                entity = NextbotAngryMunci(self.world, spawn_pos)
                self.created_entities.append(entity)
                self.world.add_entity(entity)
                break

    def onBlockCollision(self, block):
        super().onBlockCollision(block)
        if self.can_damage_block:
            block.damage(4)
            self.can_damage_block = False
            self.block_break_timer.reset()

    def onBombExplosionCollision(self, bomb):
        if bomb.can_damage:
            self.damage(200)
            bomb.can_damage = False

    def on_death(self):
        # Killing all summoned bots
        for entity in self.created_entities:
            entity.destroy()
        
        # Playing death sound
        sound_volume = calculate_sound_volume(self.position, self.world.player.position, 1500)
        self.death_sound.play_once(sound_volume)

        self.destroy()

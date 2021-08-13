import pygame
from pygame.constants import K_LEFT, K_RIGHT
screen_height = 700
screen_width = 900

RED = (255, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(
            'graphics/Tennisball.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.y_velocity = -4
        self.x_velocity = 0

    def ready_state(self, ready_status, x):
        if ready_status:
            self.rect.x = x+40

    def update(self, ready_state, player_x_velocity, player_sprite):
        if ready_state:
            if self.bar_moving():
                self.x_velocity = player_x_velocity
            else:
                self.x_velocity = 0
        if not ready_state:
            self.move_ball()
            self.bar_bounce(player_sprite)
            self.wasted(player_sprite)

    def bar_moving(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] or keys[K_RIGHT]:
            return True
        else:
            return False

    def bar_bounce(self, bar):
        if self.rect.colliderect(bar.rect):
            self.y_velocity = -self.y_velocity

            if self.bar_moving():
                self.x_velocity = bar.x_velocity
            else:
                self.x_velocity = self.x_velocity

    def bounce_y(self):
        if self.rect.y <= 0:
            self.y_velocity = -self.y_velocity

    def bounce_x(self):
        if self.rect.x <= 0:
            self.x_velocity = -self.x_velocity

        if self.rect.x >= screen_width-30:
            self.x_velocity = -self.x_velocity

    def move_ball(self):
        self.bounce_y()
        self.bounce_x()
        self.rect.y += self.y_velocity
        self.rect.x += self.x_velocity

    def wasted(self, player_spirit):
        if self.rect.y == screen_height+30:
            player_spirit.wasted()
            pos = (screen_width/2, screen_height-30)
            self.rect = self.image.get_rect(midbottom=pos)
            self.x_velocity = 0

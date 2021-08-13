
import pygame
WHITE = (255, 255, 255)
RED = (255, 20, 0)


class Brick(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((100, 30))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(midbottom=pos)
        self.lives = 2

    def update(self, ball_sprite):
        self.change_color()
        self.ball_hit(ball_sprite)
        if self.lives == 0:
            self.kill()

    def change_color(self):
        if self.lives < 2:
            self.surf.fill(RED)

    def ball_hit(self, ball_sprite):
        if self.rect.colliderect(ball_sprite):
            if self.rect.collidepoint(ball_sprite.rect.midtop):
                ball_sprite.y_velocity = ball_sprite.y_velocity*-1
                self.lives -= 1
            elif self.rect.collidepoint(ball_sprite.rect.midbottom):
                ball_sprite.y_velocity = ball_sprite.y_velocity*-1
                self.lives -= 1
            elif self.rect.collidepoint(ball_sprite.rect.midright):
                ball_sprite.x_velocity = ball_sprite.x_velocity*-1
                self.lives -= 1
            elif self.rect.collidepoint(ball_sprite.rect.midleft):
                ball_sprite.x_velocity = ball_sprite.x_velocity*-1
                self.lives -= 1

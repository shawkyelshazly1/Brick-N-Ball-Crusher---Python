from brick import Brick
from ball import Ball
from player import Player
import pygame
import sys


class Game:
    def __init__(self):
        self.player_sprite = Player(
            (screen_width/2, screen_height-10), screen_width)
        self.player = pygame.sprite.GroupSingle(self.player_sprite)
        self.ball_sprite = Ball(
            (screen_width/2, screen_height-30))
        self.ball = pygame.sprite.GroupSingle(self.ball_sprite)
        self.bricks = pygame.sprite.Group()

        for r in range(1, 9):
            for c in range(1, 8):
                brick_sprite = Brick(((c*105)+30, (r*35)+100))
                self.bricks.add(brick_sprite)

    def run(self):
        self.player.update()
        screen.blit(self.player_sprite.surf, self.player_sprite.rect)

        self.ball.draw(screen)
        self.ball_sprite.ready_state(
            self.player_sprite.ready, self.player_sprite.rect.x)
        player_sprite_location = (
            self.player_sprite.rect.x, self.player_sprite.rect.y)
        self.ball_sprite.update(self.player_sprite.ready,
                                self.player_sprite.x_velocity, self.player_sprite)

        for brick in self.bricks:
            screen.blit(brick.surf, brick.rect)

        self.bricks.update(self.ball_sprite)


if __name__ == '__main__':
    pygame.init()
    screen_height = 700
    screen_width = 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60)

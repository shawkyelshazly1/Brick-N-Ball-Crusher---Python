import pygame

WHITE = (255, 255, 255)
screen_height = 700
screen_width = 900


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, screen_limit):
        super().__init__()
        self.surf = pygame.Surface((120, 20))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(midbottom=pos)
        self.max_X = screen_limit
        self.ready = True
        self.x_velocity = 0

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x_velocity = 5
            self.rect.x += self.x_velocity

        if keys[pygame.K_LEFT]:
            self.x_velocity = -5
            self.rect.x += self.x_velocity

        if keys[pygame.K_SPACE]:
            self.shoot_ball()

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= self.max_X:
            self.rect.right = self.max_X

    def shoot_ball(self):
        self.ready = False

    def update(self):
        self.get_input()
        self.constraint()

    def wasted(self):
        pos = (screen_width/2, screen_height-10)
        self.rect = self.surf.get_rect(midbottom=pos)
        self.ready = True
        self.x_velocity = 0

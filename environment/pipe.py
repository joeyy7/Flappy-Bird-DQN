import pygame
import numpy as np

RANDOM_PIPES = [150, 250, 350, 450, 550]


class Pipe:

    def __init__(self, screen, s_width, s_height, color, dist_between_pipes=220,pipe_image_up=None, pipe_image_down=None):

        self.pipe_image_up = pipe_image_up  # 52x808
        self.pipe_image_down = pipe_image_down  # 52x808

        self.screen = screen
        self.s_width = s_width
        self.s_height = s_height
        self.color = color

        self.top = np.random.choice(RANDOM_PIPES)
        self.bot = self.top + dist_between_pipes

        # self.top = random.randrange(120, s_height-370)
        # self.bot = self.top + 350

        self.width = 52
        self.speed = 3
        self.x = s_width
        self.within_pipe = False

    def draw(self):
        # rect_top = pygame.rect.Rect(self.x, 0, self.width, self.top)
        # rect_bot = pygame.rect.Rect(self.x, self.bot, self.width, self.s_height)
        # pygame.draw.rect(self.screen, self.color, rect_top)
        # pygame.draw.rect(self.screen, self.color, rect_bot)

        if self.top > 320:
            pipe_rotated = pygame.transform.rotate(self.pipe_image_up, 180)
            self.screen.blit(pipe_rotated, (self.x, self.top - 320))
            pipe_rotated_long = pygame.transform.rotate(
                self.pipe_image_down, 180)
            self.screen.blit(pipe_rotated_long, (self.x, self.top - 320 - 280))
        else:
            pipe_rotated = pygame.transform.rotate(self.pipe_image_up, 180)
            self.screen.blit(pipe_rotated, (self.x, self.top - 320))

        if self.s_height - self.bot > 320:
            self.screen.blit(self.pipe_image_up, (self.x, self.bot))
            self.screen.blit(self.pipe_image_down, (self.x, self.bot + 280))
        else:
            self.screen.blit(self.pipe_image_up, (self.x, self.bot))

    def update(self):
        self.x -= self.speed

    def hits(self, bird):
        if bird.y < self.top or bird.y > self.bot:
            if self.x < bird.x < self.x + self.width:
                return True

    def behind(self, bird):
        if bird.x > self.x + self.width and not self.within_pipe:
            self.within_pipe = True
            return True
        if bird.x < self.x + self.width:
            self.within_pipe = False

    def off_screen(self):
        return self.x + self.width + 5 < 0

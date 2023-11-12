import pygame as pg


class Ball:

    def __init__(self, window):
        self.window = window

        self.rect = pg.Rect(400, 250, 16, 16)
        self.move_x = -3
        self.move_y = -3

    def draw_ball(self):
        pg.draw.rect(self.window, "#FAD586", self.rect, 0, 10)

    def move(self):

        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def bounce(self, line, paddle_r, paddle_l):
        if self.rect.colliderect((0, 500, 800, 2)) or self.rect.colliderect(line):
            self.move_y *= -1
        if self.rect.colliderect(paddle_r) or self.rect.colliderect(paddle_l):
            self.move_x *= -1

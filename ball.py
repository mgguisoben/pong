import pygame as pg


class Ball:

    def __init__(self, window):
        self.window = window

        self.ball = pg.Rect(400, 250, 16, 16)
        self.move_x = -3
        self.move_y = -3

    def draw_ball(self):
        pg.draw.rect(self.window, "#FAD586", self.ball, 0, 10)

    def move(self):

        self.ball.x += self.move_x
        self.ball.y += self.move_y

    def bounce(self, line, paddle_r, paddle_l):
        if self.ball.colliderect((0, 500, 800, 2)) or self.ball.colliderect(line):
            self.move_y *= -1
        if self.ball.colliderect(paddle_r) or self.ball.colliderect(paddle_l):
            self.move_x *= -1

import pygame as pg


class Paddle:

    def __init__(self, window):
        self.window = window
        self.width = self.window.get_width()
        self.paddles = []

        self.create_paddle()

        self.move_up1 = False
        self.move_down1 = False
        self.move_up2 = False
        self.move_down2 = False

    def create_paddle(self):
        for x in range(2):
            rect = pg.Rect(0, 0, 10, 100)
            rect.center = (abs(self.width * x - 40), 250)
            self.paddles.append(rect)

    def draw_paddle(self):
        for paddle in self.paddles:
            pg.draw.rect(self.window, "white", paddle)

    def handle_events1(self, event):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.move_up1 = True
            elif event.key == pg.K_DOWN:
                self.move_down1 = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.move_up1 = False
            elif event.key == pg.K_DOWN:
                self.move_down1 = False

    def handle_events2(self, event):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.move_up2 = True
            elif event.key == pg.K_s:
                self.move_down2 = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                self.move_up2 = False
            elif event.key == pg.K_s:
                self.move_down2 = False

    def move1(self, line):
        if self.move_up1 and not self.paddles[1].colliderect(line):
            self.paddles[1].y -= 10
        elif self.move_down1 and not self.paddles[1].colliderect((0, 500, 800, 2)):
            self.paddles[1].y += 10

    def move2(self, line):
        if self.move_up2 and not self.paddles[0].colliderect(line):
            self.paddles[0].y -= 10
        elif self.move_down2 and not self.paddles[0].colliderect((0, 500, 800, 2)):
            self.paddles[0].y += 10

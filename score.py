import pygame as pg


class ScoreBoard:

    def __init__(self, window):
        self.window = window

    def draw_line(self):
        return pg.draw.line(self.window, "white", (0, 40), (800, 40), 2)

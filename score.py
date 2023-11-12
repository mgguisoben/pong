import pygame as pg

pg.font.init()


class ScoreBoard:

    def __init__(self, window, font_fp):
        self.window = window
        self.font = pg.font.Font(font_fp, 40)

        self.score_r = 0
        self.score_l = 0
        self.space = " "

    def draw_line(self):
        return pg.draw.line(self.window, "white", (0, 40), (800, 40), 2)

    def draw_score(self):
        text = f"{self.score_l}{self.space * 50}P O N G{self.space * 50}{self.score_r}"
        score_text = self.font.render(text, False, "white")
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (400, 25)
        self.window.blit(score_text, score_text_rect)

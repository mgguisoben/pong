import pygame as pg

from paddle import Paddle
from score import ScoreBoard

pg.init()
pg.display.set_caption("P O N G")

clock = pg.time.Clock()

window = pg.display.set_mode((800, 500))
score_ = ScoreBoard(window)

paddle = Paddle(window)

running = True

while running:

    window.fill("black")

    line = score_.draw_line()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        paddle.handle_events1(event)
        paddle.handle_events2(event)

    paddle.move1(line)
    paddle.move2(line)

    paddle.draw_paddle()

    pg.display.update()

    clock.tick(60)

pg.quit()

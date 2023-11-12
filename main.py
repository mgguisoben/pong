import pygame as pg

from ball import Ball
from paddle import Paddle
from score import ScoreBoard

FONT_FP = "assets/font/MyGirlIsRetro-0Grz.ttf"


def reset_ball():
    new_ball = Ball(window)
    new_ball.move_x *= -1
    new_ball.move_y *= -1
    return new_ball


pg.init()
pg.display.set_caption("P O N G")
window = pg.display.set_mode((800, 500))
clock = pg.time.Clock()
score_ = ScoreBoard(window, FONT_FP)
paddle = Paddle(window)
ball_ = Ball(window)

running = True

while running:

    window.fill("black")

    line = score_.draw_line()

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

        paddle.handle_events1(event)
        paddle.handle_events2(event)

    # paddle.move1(line)
    paddle.move2(line)
    paddle.move_ai(ball_.ball, line)
    ball_.move()

    paddle.draw_paddle()
    ball_.draw_ball()
    score_.draw_score()

    ball_.bounce(line, paddle.paddles[0], paddle.paddles[1])

    if ball_.ball.x > 800:
        ball_ = reset_ball()
        score_.score_l += 1

    elif ball_.ball.x < 0:
        ball_ = reset_ball()
        score_.score_r += 1

    pg.display.update()

    clock.tick(60)

pg.quit()

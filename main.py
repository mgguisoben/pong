import pygame as pg

pg.init()
pg.display.set_caption("P O N G")

window = pg.display.set_mode((800, 500))

running = True

while running:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()

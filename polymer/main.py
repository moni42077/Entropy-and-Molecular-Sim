import pygame as pg 

def generate_chain(N,b):
    


BLACK = (0, 0, 0)
ORANGE = (237, 85, 59)
BLUE = (6, 133, 135)


pg.init()
X = 800
Y = 800
N = 10
SCREEN = pg.display.set_mode((X, Y))
CLOCK = pg.time.Clock()
SCREEN.fill(BLACK)


while True:
    SCREEN.fill(BLUE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    pg.display.update()
    CLOCK.tick(60)


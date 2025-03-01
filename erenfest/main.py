import numpy as np
import pygame as pg
from particle import Particle   

def generate_particles(n):
    for i in range(n):
        pg.draw.circle(SCREEN,ORANGE,(np.random.rand() *X ,np.random.rand() * Y ),10)

def draw_wall(arr):
    x0,y0,x1,y1 = arr
    pg.draw.line(SCREEN,BLACK,(x0,y0),(x1,y1),width=4)

BLACK = (0, 0, 0)
ORANGE = (237, 85, 59)
BLUE = (6, 133, 135)


pg.init()
X = 800
Y = 800
N = 50
SCREEN = pg.display.set_mode((X, Y))
CLOCK = pg.time.Clock()
SCREEN.fill(BLACK)


walls = [[X/2,0,X/2,Y/3],[X/2,2*Y/3,X/2,Y]]

#generate_particles(N)
particles = [Particle(np.random.rand()*(X/2-20),np.random.rand()*(Y-20),10,ORANGE,np.random.uniform(-2,2,1)[0],np.random.uniform(-2,2,1)[0]) for _ in range(N)]
while True:
    SCREEN.fill(BLUE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
    
    for p in particles:
        p.draw(SCREEN)
        draw_wall(walls[0])
        draw_wall(walls[1])
        p.move(X,Y,walls)

    #draw walls
    draw_wall(walls[0])
    draw_wall(walls[1])


    pg.display.update()
    CLOCK.tick(60)


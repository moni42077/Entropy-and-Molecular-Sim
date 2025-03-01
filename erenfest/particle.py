import pygame as pg

class Particle:
    def __init__(self,x,y,radius,color,speed_x,speed_y):
        self.x = x
        self.y = y
        self.r = radius
        self.c = color
        self.vx = speed_x
        self.vy = speed_y

    def draw(self,screen):
        pg.draw.circle(screen,self.c,(int(self.x), int(self.y)), self.r)

    def move(self,width,height,walls=None):
        #walls = [[x0,y0,x1,y1] , [x2,y2,x3,y3] ... meaning a wall from (x0,y0) to (x1,y1) ^ (x2,y2) to (x3,y3) etc
        self.x += self.vx
        self.y += self.vy

        #Bounce from wall
        if self.x - self.r < 0 or self.x + self.r  > width:
            self.vx *= -1
        
        if self.y - self.r < 0 or self.y + self.r > height:
            self.vy *= -1

        if walls != None:
            #Check if it collides with custom wall
            for wall in walls:
                #wall = [x0,y0,x1,y1]
                #Horizontal wall check i.e. y0 == y1
                if wall[1] == wall[3]: 
                    if wall[0] <= self.x <= wall[2]:  # Ensure the particle is within the wall's x-bounds
                        if self.y - self.r <= wall[1] <= self.y + self.r:  # Check y collision
                            self.vy *= -1
                elif wall[0] == wall[2]: 
                    if wall[1] <= self.y <= wall[3]:  # Ensure the particle is within the wall's y-bounds
                        if self.x - self.r <= wall[0] <= self.x + self.r:  # Check x collision
                            self.vx *= -1
                else:
                    #Angled line mx + c
                    #Check if the particle is even close to the line i.e. in a square for which this wall is a diagonal
                    continue #TODO implement this later as we dont need it for now

import random
import pygame

def once(time):

    pass
    
class food():
    
    def __init__(self, snake):

        self.snake = snake
        self.pos   = random.choice([x for x in grid for y in snake.body if x != y])
        self.color = (255, 0, 0)

    def render(self):

        pygame.draw.rect(self.snake.window, self.color, (self.pos[0]*pixel, self.pos[1]*pixel, pixel, pixel))

class snake():

    LEFT  = [-1, 0]
    RIGHT = [1, 0]
    UP    = [0, -1]
    DOWN  = [0, 1]

    def __init__(self, window):

        self.body   = [[round(xbound/2), round(ybound/2)]]
        self.window = window
        self.color  = (0, 0, 0)
        self.food   = food(self)
        self.vel    = snake.UP

    def collide(self):

        for b in self.body.copy().pop(-1):
            if b == self.body[0]:
                print("return True")
            
        return False

    def teleport(self):

        if self.body[-1][0] > xbound: self.body[-1][0] = 0
        if self.body[-1][0] < 0     : self.body[-1][0] = xbound
        if self.body[-1][1] > ybound: self.body[-1][1] = 0
        if self.body[-1][1] < 0     : self.body[-1][1] = ybound

    def turn(self, direction):

        self.vel = direction

        
    def update(self):

        self.body.append([self.body[-1][0]+self.vel[0], self.body[-1][1]+self.vel[1]])
        if (self.body[-1] != self.food.pos): self.body.remove(self.body[0])
        else                              : self.food = food(self)

    def render(self):

        self.food.render()

        for x in self.body:
            pygame.draw.rect(self.window, self.color, (x[0]*pixel , x[1]*pixel, pixel, pixel))




xbound = 50
ybound = 50
pixel  = 10

win     = pygame.display.set_mode((xbound*pixel , ybound*pixel))
grid    = [[x, y] for x in range(xbound) for y in range(ybound)]

snek = snake(win)

RUN = True
    
while RUN:

    
    snek.render()
    snek.update()
    

    keys = pygame.key.get_pressed()
    
    if   keys[pygame.K_LEFT] : snek.turn(snake.LEFT)
    elif keys[pygame.K_RIGHT]: snek.turn(snake.RIGHT)
    elif keys[pygame.K_UP]   : snek.turn(snake.UP)
    elif keys[pygame.K_DOWN] : snek.turn(snake.DOWN)

    snek.teleport()
    
    pygame.display.update()
    pygame.time.Clock().tick(30)

    win.fill((255, 255, 255))

    if snek.collide(): RUN = False

    for e in pygame.event.get():
        if e.type == pygame.QUIT: RUN = False 

pygame.quit()


import pygame
import random
from engine import *


def check_collision(obj):
    if (obj.x < 90 ):
        if(obj.y - obj.h < y_position):
            return True
    return False

pygame.init()

win = pygame.display.set_mode((1000,300))
obj = Object()

clr = [127,127,127]

y_position = 250
y_velocity = 0
run = True
jump_status = False

energy = 70
counter = 0
while run == True:
    
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if(obj.x < 90 and obj.x > 50 or obj.x+obj.w < 90 and obj.x+obj.w>50):
        if(obj.y-obj.h < y_position):
            break

    if(energy == 0):
        print('U ded')
        break
    obj.move(energy)


    if(counter == 20):
        energy-= 1
        counter = 0
        print(energy)
    else:
        counter += 1

    if keys[pygame.K_SPACE]:
        if(not jump_status):
            jump_status = True
            y_velocity = 34
    if keys[pygame.K_m]:
        counter = 0
        if(energy < 70):
            energy += 30
        else:
            energy = 100

    

    if(jump_status):
        y_velocity -= 2

    y_position -= y_velocity

    if(y_position >= 250):
        jump_status = False
        y_velocity = 0        
    
    

    clr[0] += random.randint(-6,6) if clr[0] > 6 and clr[0] < 249 else 0
    if(clr[0] < 6 or clr[0]>249):
        clr[0] = 127
        
        clr[1] += random.randint(-6,6) if clr[1] > 6 and clr[1] < 249 else 0
        if(clr[1] < 6 or clr[1]>249):
            clr[1] = 127
        
        clr[2] += random.randint(-6,6) if clr[2] > 6 and clr[2] < 249 else 0
        if(clr[2] < 6 or clr[2]>249):
            clr[2] = 127
    

    win.fill(tuple(clr))
    pygame.draw.rect(win,obj.color,(obj.x,obj.y,obj.w,obj.h))
    pygame.draw.rect(win,(50,200,80),(50,y_position,40,60))
    pygame.display.update()


pygame.quit()



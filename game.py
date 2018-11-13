import pygame
import random
from engine import *


def check_collision(obj):
    if(obj.x < 90 and obj.x > 50 or obj.x+obj.w < 90 and obj.x+obj.w>50):
        if(obj.y-obj.h < y_position):
            return True
    return False


def check_projectile_collision(proj, obj):
    if(obj.x <= proj.x):
        if(proj.y > obj.y and proj.x < obj.x+obj.h):
            return True
    return False



pygame.init()

win = pygame.display.set_mode((1000,300))


obj_coord = [2100,2500,2700,2800]

clr = [127,127,127]

y_position = 250
y_velocity = 0
run = True
jump_status = False

energy = 100
counter = 0
heal = False
armed = False
arming = False
shoot = False
projectiles = []
objects = []
velocity = -3
distance_run = 0
ending = obj_coord[-1]
while run == True:
    if(distance_run > ending + 2500 ):
        print("U win")
        run = False
    if(len(obj_coord)>0):
        if(distance_run + 900 > obj_coord[0]):
            objects.append(Object(obj_coord[0]))
            obj_coord.pop(0)
    distance_run -= velocity
    print(distance_run)
    velocity = int(-10 * (energy+10)/100)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

    for obj in objects:
        if(obj.x <= -20):
            objects.remove(obj)
        if check_collision(obj):
            run = False
        draw = True
        for proj in projectiles:
            if check_projectile_collision(proj,obj):
                objects.remove(obj)
                projectiles.remove(proj)
                draw = False
        if draw:
            pygame.draw.rect(win,obj.color,(obj.x,obj.y,obj.w,obj.h))
        obj.move(velocity)


    if(energy == 0):
        print('U ded')
        break
    #obj.move(energy)


    if(counter == 50):
        energy -= 1
        counter = 0
    else:
        counter += 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_n]:
        if(not arming):
            arming = True
            armed = True
    else:
        arming = False    

        
    if not armed:
        if keys[pygame.K_SPACE]:
            if(not jump_status):
                jump_status = True
                y_velocity = 34
    else:
        pygame.draw.rect(win,(255,0,0),(50,50,10,10))
        if keys[pygame.K_m]:
            if(not heal):
                armed = False
                heal = True
                counter = 0
                if(energy  > 70):
                    energy = 100
                else:
                    energy += 30
        else:
            heal = False
        if keys[pygame.K_b]:
            if(not shooting):
                shooting = True
                armed = False
                p = Projectile(y_position)
                projectiles.append(p)
        else: 
            shooting = False



    for p in projectiles:
        p.move()
        pygame.draw.rect(win,(127,0,0),(p.x,p.y,p.side,p.side,))

    if(jump_status):
        y_velocity -= 2

    y_position -= y_velocity

    if(y_position >= 250):
        jump_status = False
        y_velocity = 0        
    
    
    pygame.draw.rect(win,(50,200,80),(50,y_position,40,60))
    pygame.display.update()

pygame.time.delay(1000)
pygame.quit()



import pygame
from engine import *


pygame.init()

win = pygame.display.set_mode((1000,300))


obj_coord = [1000,1800,2500,2700,2800,3000, 3500,4000,4400,4800,5000]

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
shooting = False
start = obj_coord[0]
ending = obj_coord[-1]

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    if(not run):
        break
    
    
    velocity = int(-15 * (energy+10)/100)
    distance_run,run = update_distance(distance_run,velocity,ending)
    if(not run):
        break
    print(distance_run)
    pygame.time.delay(10)

    clr = change_colors(clr)
    

    win.fill(tuple(clr))


    projectiles = move_projectiles(projectiles,win)
    objects,run = move_objects(objects,projectiles,y_position,velocity,win)
    if(not run):
        break

    objects,obj_coord = update_objects(objects,obj_coord,distance_run)
    counter,energy,run = update_energy(counter,energy)
    if(not run):
        break
    
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
                energy -= 1
        else: 
            shooting = False


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



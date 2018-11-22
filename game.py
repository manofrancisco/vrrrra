import pygame
from engine import *
import time


pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

pygame.init()


clr = [127,127,127]
clr = change_colors(clr)
win = pygame.display.set_mode((1000,500))
win.fill(tuple(clr))


key_dict ={'A':pygame.K_a,'B':pygame.K_b,'C':pygame.K_c,'D':pygame.K_d,'E':pygame.K_e,
    'F':pygame.K_f, 'G':pygame.K_g,'H':pygame.K_h,'I':pygame.K_i,'J':pygame.K_j,'K':pygame.K_k,'L':pygame.K_l,'M':pygame.K_m,'N':pygame.K_n,'O':pygame.K_o,'P':pygame.K_p,
    'Q':pygame.K_q,'R':pygame.K_r,'S':pygame.K_s,'T':pygame.K_t,'U':pygame.K_u,'V':pygame.K_v,'W':pygame.K_w,'X':pygame.K_x,'Y':pygame.K_y,'Z':pygame.K_z}

available = list(key_dict.keys())
print(available)

index = random.randint(0,len(available)-1)
jump_letter = available[index]
jump = key_dict[available[index]]
available.pop(index)
index = random.randint(0,len(available)-1)
prep_letter = available[index]
prep = key_dict[available[index]]
available.pop(index)
index = random.randint(0,len(available)-1)
shoot_letter = available[index]
shoot = key_dict[available[index]]
available.pop(index)
index = random.randint(0,len(available)-1)
heal_letter = available[index]
heal = key_dict[available[index]]
available.pop(index)

myfont = pygame.font.SysFont('Arial Bold', 30)
initString = 'Hey, to play press  Enter, '+jump_letter+' to jump, '+ prep_letter +' to Prep  '+ shoot_letter +' to shoot and '+ heal_letter +' to heal'
textsurface = myfont.render(initString, False, (0, 0, 0))

win.blit(textsurface,(100,300))
pygame.display.update()
run = True
quit = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit = True
    k = pygame.key.get_pressed()
    if(k[pygame.K_KP_ENTER]):
        print(pygame.K_KP_ENTER)
        print('starting game')
        break    

if quit:
    pygame.quit()
if not quit:
    obj_coord = [1000,1800,2500,2700,2800,3000, 3500,4000,4400,5000]
    f_coord = [(1500,390),(2000,250)]

    y_position = 450
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
    floats = []
    velocity = -3
    distance_run = 0
    shooting = False
    start = obj_coord[0]
    ending = max(obj_coord[-1],f_coord[-1][0])
    ending = 10000

    start = time.time()
    while run :
        print(len(pygame.event.get()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        if(not run):
            break
        
        
        velocity = int(-8* (energy+10)/100)
        distance_run,run = update_distance(distance_run,velocity,ending)
        if(not run):
            break
        pygame.time.delay(10)

        clr = change_colors(clr)
        win.fill(tuple(clr))
        curr = time.time()
        
        textsurface = myfont.render(str(curr-start), False, (0, 0, 0))

        win.blit(textsurface,(0,0))


        projectiles = move_projectiles(projectiles,win)
        objects,run = move_objects(objects,projectiles,y_position,velocity,win)
        if(not run):
            break
        floats,run = move_floats(floats,projectiles,velocity,y_position,win)
        if(not run):
            break

        objects,obj_coord = update_objects(objects,obj_coord,distance_run)

        floats,f_coord = update_floats(floats,f_coord,distance_run)

        counter,energy,run = update_energy(counter,energy)
        if(not run):
            break
        
        keys = pygame.key.get_pressed()
        
        if keys[prep]:
            if(not arming):
                arming = True
                armed = True
        else:
            arming = False    
        
        if not armed:
            if keys[jump]:
                if(not jump_status):
                    jump_status = True
                    y_velocity = 30
        else:
            pygame.draw.rect(win,(255,0,0),(50,50,10,10))
            if keys[heal]:
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
            if keys[shoot]:
                if(not shooting):
                    shooting = True
                    armed = False
                    p = Projectile(y_position)
                    projectiles.append(p)
                    energy -= 1
            else: 
                shooting = False


        if(jump_status):
            y_velocity -= 1

        y_position -= y_velocity

        if(y_position >= 450):
            jump_status = False
            y_velocity = 0        
        
        
        pygame.draw.rect(win,(50,200,80),(50,y_position,40,60))
        pygame.display.update()


    
    
    pygame.time.delay(1000)
    pygame.quit()



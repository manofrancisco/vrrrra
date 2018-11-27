import pygame
from engine import *
import time




pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

pygame.init()


clr = [127,127,127]
clr = change_colors(clr)
screen_size = 800
win = pygame.display.set_mode((1000,screen_size))
win.fill(tuple(clr))


key_dict ={'A':pygame.K_a,'B':pygame.K_b,'C':pygame.K_c,'D':pygame.K_d,'E':pygame.K_e,
    'F':pygame.K_f, 'G':pygame.K_g,'H':pygame.K_h,'I':pygame.K_i,'J':pygame.K_j,'K':pygame.K_k,'L':pygame.K_l,'M':pygame.K_m,'N':pygame.K_n,'O':pygame.K_o,'P':pygame.K_p,
    'Q':pygame.K_q,'R':pygame.K_r,'S':pygame.K_s,'T':pygame.K_t,'U':pygame.K_u,'V':pygame.K_v,'W':pygame.K_w,'X':pygame.K_x,'Y':pygame.K_y,'Z':pygame.K_z}

available = list(key_dict.keys())

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
shoot_key = key_dict[shoot_letter]
available.pop(index)
index = random.randint(0,len(available)-1)
heal_letter = available[index]
heal_key = key_dict[available[index]]
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
    if(k[pygame.K_RETURN] or k[pygame.K_KP_ENTER]):
        break    

if quit:
    pygame.quit()
if not quit:
    obj_coord = [1000,1800,2500,2800,3000, 3500,4000,4400,5000,5200,5400,6000,7000,7500,8000]
    f_coord = [(1500,590),(2000,450),(2300,600),(3100,750),(3800,650),(4100,550),(4200,500),(4350,600),(5100,550),(5200,500),(5350,600),(5800,550),(6200,600),(6300,600),(6400,500),(6900,550),(7100,550),(7300,550),(7700,650)]

    y_position = screen_size - 100
    y_velocity = 0
    run = True
    jump_status = False

    energy = 100
    counter = 0
    heal = False
    armed = False
    arming = False
    shoot = False
    shooting = False
    projectiles = []
    objects = []
    floats = []
    velocity = -3
    distance_run = 0
    shooting = False
    start = obj_coord[0]
    ending = max(obj_coord[-1],f_coord[-1][0])
    ending = 10000
    curr = 0
    start = time.time()
    lose = False
    while run :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.time.delay(100)
                pygame.quit()
            
        if(not run):
            lose = True
            break
        
        if(distance_run == 1000):
            pygame.time.delay(10000)
        
        velocity = int(-7* (energy+10)/100)
        distance_run,run = update_distance(distance_run,velocity,ending)
        if(not run):
            lose = True
            break
        pygame.time.delay(10)

        clr = change_colors(clr)
        win.fill(tuple(clr))
        curr = time.time()
        
        textsurface = myfont.render(str(curr-start) , False, (0, 0, 0))
        win.blit(textsurface,(0,0))
        txtsrf = myfont.render(jump_letter+'-jump '+ prep_letter +'-prep  '+ shoot_letter +'-shoot '+ heal_letter +'-heal',False,(0,0,0) )
        win.blit(txtsrf,(500,0))

        projectiles = move_projectiles(projectiles,win)
        objects,run = move_objects(objects,projectiles,y_position,velocity,win)
        if(not run):
            lose = True
            break
        floats,run = move_floats(floats,projectiles,velocity,y_position,win)
        if(not run):
            lose = True         
            break

        objects,obj_coord = update_objects(objects,obj_coord,distance_run,screen_size-100)

        floats,f_coord = update_floats(floats,f_coord,distance_run)

        counter,energy,run = update_energy(counter,energy)
        if(not run):
            lose = True            
            break
        
        keys = pygame.key.get_pressed()
        


        if keys[jump]:
            if(not jump_status):
                jump_status = True
                y_velocity = 30
        if keys[prep]:
            if(not arming):
                arming = True
                armed = True
        else:
            arming = False   
        
        if(armed):
            pygame.draw.rect(win,(255,0,0),(50,50,10,10))

        
        if armed:
            if keys[heal_key]:
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

            if keys[shoot_key]:
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

        if(y_position >= screen_size - 100):
            jump_status = False
            y_velocity = 0        
        
        
        pygame.draw.rect(win,(50,200,80),(50,y_position,40,60))
        pygame.display.update()

    win.fill(tuple(clr))
    if(not lose):
        myfont = pygame.font.SysFont('Arial Bold', 30)
        initString = 'You win in '+ time
        textsurface = myfont.render(initString, False, (0, 0, 0))
        win.blit(textsurface,(100,300))
        pygame.display.update()
    else:
        myfont = pygame.font.SysFont('Arial Bold', 30)
        initString = 'You lose mate'
        textsurface = myfont.render(initString, False, (0, 0, 0))
        win.blit(textsurface,(100,300))
        pygame.display.update()



    print(shoot)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.time.delay(100)
                pygame.quit()



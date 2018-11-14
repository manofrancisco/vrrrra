import random
import pygame


class Object:
    def __init__(self,x):
        self.x=x
        self.y=250
        self.w=40
        self.h=60
        self.color = (0,0,200)

    def move(self,velocity):
        self.x = self.x + velocity
        

class Projectile:
    side = 15
    def __init__(self,y_position):
        self.x = 80
        self.y = y_position +10  
        self.v = 10
        
    def move(self):
        if(self.x > 1000):
            self.y = 0
        else:
            self.x += self.v 
    
class Float:
    y = 250
    def __init__(self,x):
        self.x=x
        self.y=250
        self.w=40
        self.h=60
        self.color = (0,100,200)
    def move(self,velocity):
        self.x = self.x + velocity




def check_object_collision(obj,y_position):
    if(obj.x < 90 and obj.x > 50 or obj.x+obj.w < 90 and obj.x+obj.w>50):
        if(obj.y-obj.h < y_position):
            return True
    return False


def check_projectile_collision(proj, obj):
    if(obj.x <= proj.x):
        if(proj.y > obj.y and proj.x < obj.x+obj.h):
            return True
    return False


def change_colors(clr):
    clr[0] += random.randint(-6,6) if clr[0] > 6 and clr[0] < 249 else 0
    if(clr[0] < 6 or clr[0]>249):
        clr[0] = 127
        
        clr[1] += random.randint(-6,6) if clr[1] > 6 and clr[1] < 249 else 0
        if(clr[1] < 6 or clr[1]>249):
            clr[1] = 127
        
        clr[2] += random.randint(-6,6) if clr[2] > 6 and clr[2] < 249 else 0
        if(clr[2] < 6 or clr[2]>249):
            clr[2] = 127
    return clr


def move_projectiles(projectiles,win):    
        for p in projectiles:
            p.move()
            pygame.draw.rect(win,(127,0,0),(p.x,p.y,p.side,p.side,))
        return projectiles


def move_objects(objects,projectiles,y_position,velocity,win):
    run = True
    for obj in objects:
        if(obj.x <= -20):
            objects.remove(obj)
        if check_object_collision(obj,y_position):
            print("col")
            return objects,False
        draw = True
        for proj in projectiles:
            if check_projectile_collision(proj,obj):
                objects.remove(obj)
                projectiles.remove(proj)
                draw = False
        if draw:
            pygame.draw.rect(win,obj.color,(obj.x,obj.y,obj.w,obj.h))
        obj.move(velocity)
    return objects,run


def update_energy(counter,energy):
    run = True
    if(energy == 0):
        print('U ded')
        run = False
    if(counter == 5):
        energy -= 1
        counter = 0
    else:
        counter += 1
    return counter,energy, run

    
def update_distance(distance_run,velocity,ending):
    run = True
    distance_run -= velocity
    if(distance_run > ending + 500):
        print("U win")
        run = False
    return distance_run,run


def update_objects(objects,obj_coord,distance_run):
    if(len(obj_coord)>0):
        if(distance_run + 900 > obj_coord[0]):
            objects.append(Object(obj_coord[0]-distance_run))
            obj_coord.pop(0)
    return objects,obj_coord
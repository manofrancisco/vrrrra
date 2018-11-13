class Object:
    def __init__(self,x):
        self.x=x
        self.y=250
        self.w=40
        self.h=60
        self.color = (0,0,200)

    def move(self,velocity):
        if(self.x  < - self.w):
            self.x = 1200
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
    
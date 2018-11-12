class Object:
    x=1200
    y=250
    w=40
    h=60
    velocity = -50
    color = (0,0,200)
    def __init__(self):
        print('Object created')

    def move(self,energy):
        if(self.x  < - self.w):
            self.x = 1200

        self.velocity = int(-15 * (energy+10)/100)
        self.x = self.x + self.velocity
        



    
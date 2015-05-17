class Triangle(object):
    Spring = 0.05
    Gravity = 0.00
    Friction = -0.9

    def __init__(self, x, y, radius, index, others):
        self.x = x
        self.y = y
        self.radius = radius
        self.index = index
        self.others = others
        self.vx = 0
        self.vy = random(0.1,1.0)

    def collide(self):
        for other in self.others[self.index:]:
            dx = other.x - self.x
            dy = other.y - self.y
            minDist = other.radius + self.radius
            if dist(other.x, other.y, self.x, self.y) < minDist:
                angle = atan2(dy, dx)
                targetX = self.x + cos(angle) * minDist
                targetY = self.y + sin(angle) * minDist
                ax = (targetX - other.x) * Ball.Spring
                ay = (targetY - other.y) * Ball.Spring
                self.vx -= ax
                self.vy -= ay
                other.vx += ax
                other.vy += ay
        

    def move(self):
        self.vy += self.Gravity
        self.x += self.vx
        self.y += self.vy

        '''
        if self.x + self.radius > width:
            self.x = width - self.radius
            #self.vx *= Ball.Friction
        elif self.x - self.radius < 0:
            self.x = self.radius
            #self.vx *= Ball.Friction
        '''
        if self.y + self.radius > height:
            self.y = random(-200,-45)#height - self.radius
            #self.vy *= Ball.Friction
        #elif self.y - self.radius < 0:
            #self.y = self.radius
            #self.vy *= Ball.Friction

    def display(self):
        triangle(self.x, self.y+self.radius,
                 self.x-sqrt(3)*self.radius/2.0,
                 self.y-self.radius/2.0,
                 self.x+sqrt(3)*self.radius/2.0,
                 self.y-self.radius/2.0)
        

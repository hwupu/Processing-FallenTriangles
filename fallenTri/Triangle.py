from ColorScheme import Color

class Triangle(object):
    Spring = 0.05
    Gravity = 0.00
    Friction = -0.001

    def __init__(self, x, y, radius, index, others):
        self.x = x
        self.y = y
        self.radius = radius
        self.index = index
        self.others = others
        self.vx = 0
        self.vy = random(0.1,1.0)
        self.color = Color.shades[int(random(3))]
        self.alpha = random(0.6, 1.0)
        self.rotate = random(0, 180)
        self.rotate_speed = random(-2.5, 2.5)

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

    @property
    def max_step(self):
        return abs(self.Gravity)

    @property
    def min_step(self):
        return -self.max_step

    def move(self):
        self.vy += self.Gravity
        if self.Gravity:
            if self.max_step > self.vy:
                self.vy = self.min_step
            elif self.max_step < self.vy:
                self.vy = self.max_step
        self.x += self.vx
        self.y += self.vy
        self.rotate += self.rotate_speed

        self.alpha += random(0.5*self.Friction,2*self.Friction)

        '''
        if self.x + self.radius > width:
            self.x = width - self.radius
            #self.vx *= Ball.Friction
        elif self.x - self.radius < 0:
            self.x = self.radius
            #self.vx *= Ball.Friction
        '''
        change_y = False
        if self.y + self.radius > height:
            change_y = random(-200, -45)   #height - self.radius
        elif self.y - self.radius < -200:
            change_y = random(455, 500)

        if change_y:
            self.x = random(-10, width + 10)
            self.y = change_y
            self.alpha = random(0.6, 1.0)

            #self.vy *= Ball.Friction
        #elif self.y - self.radius < 0:
            #self.y = self.radius
            #self.vy *= Ball.Friction


    def display(self):
        pushMatrix()
        fill(self.color,self.alpha)
        translate(self.x, self.y)
        rotate(radians(self.rotate))
        triangle(0, self.radius,
                 -sqrt(3)*self.radius/2.0,
                 -self.radius/2.0,
                 sqrt(3)*self.radius/2.0,
                 -self.radius/2.0)
        popMatrix()

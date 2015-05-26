from ColorScheme import Color
from Canvas import canvas

class Bear(object):
    
    def __init__(self, scale=1.0):
        self.scale = scale
        self.fromX = 0
        self.toX = canvas.width // 2
        self.speed = 10
        self.color = Color.orange
    
    def draw(self):
        fill(self.color)
        noStroke()

        pushMatrix()
        self.fromX += self.accel
        translate(self.fromX - self.scale // 2, -self.scale)
        ellipse(self.scale / 2.0, 0.0,
                self.scale * 2, self.scale * 2)
        ellipse(self.scale / 2.0, -self.scale * 1.25,
                self.scale * 1.5, self.scale * 1.5)
        popMatrix()


    @property
    def accel(self):
        return (self.toX - self.fromX) // self.speed
    
    @property
    def x(self):
        return self.fromX
    
    @x.setter
    def x(self, val):
        self.fromX = val


class Collision(object):
    
    def __init__(self, obj_a, obj_b):
        if obj_a.x < obj_b.x:
            self.right, self.left = obj_b, obj_a
        elif obj_a.x > obj_b.x:
            self.right, self.left = obj_a, obj_b
        else:
            self.right, self.left = obj_b, obj_a

    def detect(self):
        width = 100
        if self.right.x - width < self.left.x:
            print('collision dected!', self.left.accel, self.right.accel)
            if self.left.accel > 0 and self.left.accel > self.right.accel:
                self.left.toX = self.right.x - width * 2
            elif self.right.accel < 0 and self.left.accel > self.right.accel:
                self.right.toX = self.left.x + width * 2

from ColorScheme import Color
from Canvas import canvas

class Bear(object):
    
    def __init__(self, scale=1.0):
        self.scale = scale
        self.fromX = 0
        self.toX = canvas.width//2
        self.speed = 10
    
    def draw(self):
        fill(Color.darkBlue)
        noStroke()
        
        pushMatrix()
        self.fromX += (self.toX - self.fromX)//self.speed
        translate(self.fromX - self.scale//2, -self.scale)
        triangle(self.scale/2.0, 0.0,
                 0.0, self.scale,
                 self.scale, self.scale)
        popMatrix()


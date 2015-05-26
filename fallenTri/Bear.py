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
        self.fromX += (self.toX - self.fromX) // self.speed
        translate(self.fromX - self.scale // 2, -self.scale)
        ellipse(self.scale / 2.0, 0.0,
                self.scale * 2, self.scale * 2)
        ellipse(self.scale / 2.0, -self.scale * 1.25,
                self.scale * 1.5, self.scale * 1.5)
        popMatrix()


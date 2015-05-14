from ColorScheme import Color

class Triangle(object):
    def __init__(self, _scale=1.0):
        self.scale = _scale
        self.fromX = 0
        self.toX = 250
        self.speed = 10
    def draw(self):
        fill(Color.orange)
        noStroke()
        pushMatrix()
        deltaX = (self.toX - self.fromX)//self.speed
        self.fromX += deltaX
        translate(self.fromX, -self.scale)
        triangle(self.scale/2.0, 0.0,
                 0.0, self.scale,
                 self.scale, self.scale)
        popMatrix()


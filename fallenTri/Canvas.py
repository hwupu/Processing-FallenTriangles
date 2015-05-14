from ColorScheme import Color

class Canvas(object):
    
    def setup(self):
        size(self.width, self.height, P2D)
        
    def draw(self):
        background(Color.hay)
        fill(Color.blue)
        noStroke()
        rect(0, 2*self.height//3, self.width, self.height)

    def __init__(self, height=500, width=500):
        self.height, self.width = height, width

canvas = Canvas()

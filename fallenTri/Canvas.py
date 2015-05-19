from ColorScheme import Color

class Canvas(object):
    
    def setup(self):
        size(self.width, self.height, P2D)
        colorMode(RGB, 1.0)

    def drawBackground(self):
        background(Color.lightBlue)

    def drawStage(self):
        fill(Color.blue)
        noStroke()
        rect(0, 2*self.height//3, self.width, self.height)

        fill(Color.hay)
        textAlign(CENTER)
        textSize(10)
        text('2015, hwupu wdv4758h iblis17', self.width//2, self.height-10)
        

    def __init__(self,  width=500, height=500):
        self.height, self.width = height, width

canvas = Canvas(1000, 500)

from Canvas import canvas
import Triangle

tri = Triangle.Triangle(50.0)


def setup():
    canvas.setup()
    
 
def mouseClicked():
    tri.toX = mouseX

def draw():
    canvas.draw()
    
    pushMatrix()
    translate(0, 2*canvas.height//3)
    tri.draw()
    popMatrix()

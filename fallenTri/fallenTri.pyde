from Canvas import canvas
import Bear
import Triangle

tris = []
NUM_TRIS = 32

bear = Bear.Bear(50.0)


def setup():
    canvas.setup()
    for i in range(NUM_TRIS):
        tris.append(Triangle.Triangle(random(-10,width+10), random(-200,-45),
                          random(15, 45), i, tris))

 
def mouseClicked():
    bear.toX = mouseX

def draw():
    canvas.drawBackground()
    
    for tri in tris:
        #tri.collide()
        tri.move()
        tri.display()
    
    pushMatrix()
    translate(0, 2 * canvas.height // 3)
    bear.draw()
    popMatrix()
    
    canvas.drawStage()

from Canvas import canvas
import Bear
from Triangle import Triangle
import logging
from ColorScheme import Color

tris = []
NUM_TRIS = 32

bear = Bear.Bear(50.0)
snowman = Bear.Bear(50.0)
snowman.color = Color.white


def setup():
    canvas.setup()
    for i in range(NUM_TRIS):
        tris.append(Triangle(random(-10,width+10), random(-200,-45),
                             random(15, 45), i, tris))


def mouseClicked():
    if mouseButton == LEFT:
        snowman.toX = mouseX
    elif mouseButton == RIGHT:
        bear.toX = mouseX


def mouseWheel(event):
    Triangle.Gravity += event.getCount()
    if 20 < Triangle.Gravity:
        Triangle.Gravity = 20
    elif -20 > Triangle.Gravity:
        Triangle.Gravity = -20


def draw():
    canvas.drawBackground()

    for tri in tris:
        #tri.collide()
        tri.move()
        tri.display()

    pushMatrix()
    translate(0, 2 * canvas.height // 3)
    bear.draw()
    snowman.draw()
    popMatrix()

    canvas.drawStage()

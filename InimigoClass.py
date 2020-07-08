from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Inimigo:

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.dir=-1
        self.l=50
        self.h=50
        self.vivo=True

    def getH(self):
        return self.h

    def getL(self):
        return self.l

    def getY(self):
        return self.y

    def setY(self,temp):
        self.y=temp

    def getX(self):
        return self.x

    def setX(self,temp):
        self.x=temp

    def setDir(self,temp):
        self.dir=temp

    def setVivo(self,temp):
        self.vivo=temp

    def getVivo(self):
        return self.vivo

    def movimentar(self):
        self.x+=self.dir*3



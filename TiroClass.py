from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Tiro:

    def __init__(self,temp):
        #direção do tiro, se é positiva(player) ou negativa(inimigo)
        self.dir=temp
        self.x=0
        self.y=0
        self.atirado=False

    def getY(self):
        return self.y

    def setY(self,temp):
        self.y=temp

    def getX(self):
        return self.x

    def setX(self,temp):
        self.x=temp

    def getDir(self):
        return self.dir

    def getAtirado(self):
        return self.atirado

    def setAtirado(self,temp):
        self.atirado = temp

    def mover(self):
        self.y += self.dir * 25
        if self.y < -25:
            self.atirado = False
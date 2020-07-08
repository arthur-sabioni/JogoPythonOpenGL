from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from InimigoClass import Inimigo
from TiroClass import Tiro

class Atirador(Inimigo):

    def __init__(self,x,y):
        Inimigo.__init__(self,x,y)
        self.tiro = Tiro(-1)

    def getTiro(self):
        return self.tiro

    def atirar(self):
        self.tiro.setY(self.getY())
        self.tiro.setX(self.getX())
        self.tiro.setAtirado(True)
    
    def moverTiro(self):
        if self.tiro.atirado() == True:
            self.tiro.moverTiro()
            if self.tiro.getY() < -25:
                self.tiro.setAtirado(False)
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from TiroClass import Tiro

class Jogador:

    #3 tiros
    tiro1 = Tiro(1)
    tiro2 = Tiro(1)
    tiro3 = Tiro(1)
    tiros = [tiro1,tiro2,tiro3]

    def __init__(self):
        self.vidas = 3
        #posições na tela
        self.x=500
        self.y=70
        #largura(l) e altura(h)
        self.h=50
        self.l=50
        #movimentos direita e esquerda
        self.d=False
        self.a=False

    def getH(self):
        return self.h

    def getD(self):
        return self.d

    def getA(self):
        return self.a

    def getL(self):
        return self.l

    def getY(self):
        return self.y

    def setY(self,temp):
        self.y=temp

    def getVidas(self):
        return self.vidas

    def setVidas(self,temp):
        self.vidas=temp

    def setD(self,temp):
        self.d=temp

    def getTiros(self):
        return self.tiros

    def setA(self,temp):
        self.a=temp

    def getX(self):
        return self.x

    def setX(self,temp):
        self.x=temp

    def getAtirando(self):
        return self.atirando

    def setAtirando(self,temp):
        self.atirando=temp

    def getTiro(self):
        return self.tiro

    #movimentos do mouse, sem passar dos limites da tela
    def moverM(self,mx,my):
        if self.x<975 and self.x>25:
            self.x += (mx-self.x)/1
        elif self.x>975:
            self.x=974
        else:
            self.x=26

    #movimentos do teclado, sem passar pelos limites da tela
    def moverT(self,dir):
        if self.x < 975 and self.x>25:
            self.x += dir*20
        elif self.x>975:
            self.x=974
        else:
            self.x=26

    #atirar, checando os 3 tiros individualmente, se tiver algum para atirar, o coloca na posição do player e altera para atirado
    def atirar(self):
        for x in self.tiros:
            if x.getAtirado() == False:
                x.setAtirado(True)
                x.setX(self.x)
                x.setY(self.y)
                break

    #mover os tiros atirados, até o limite da tela
    def moverTiro(self):
        for x in self.tiros:
            if x.getAtirado() == True:
                x.mover()
                if x.getY() > 1025:
                    x.setAtirado(False)
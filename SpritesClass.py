from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

class Sprite:
    def __init__(self,x,y,h,l,textura):
        #posição do sprite
        self.x = x
        self.y = y
        #dimensões do sprite
        self.h = h
        self.l = l
        #textura
        self.textura = textura
        #print(self.textura)

    
    def getX(self):
        return self.x

    def setX(self,temp):
        self.x=temp

    def getY(self):
        return self.y

    def setY(self,temp):
        self.y=temp

    def getH(self):
        return self.h

    def setH(self,temp):
        self.h=temp

    def getL(self):
        return self.l

    def setL(self,temp):
        self.l=temp


    def getTextura(self):
        return self.textura

    def setTextura(self,temp):
        self.textura=temp

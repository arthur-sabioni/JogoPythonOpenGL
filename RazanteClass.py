from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from InimigoClass import Inimigo

class Razante(Inimigo):

    def __init__(self,x,y):
        Inimigo.__init__(self,x,y)
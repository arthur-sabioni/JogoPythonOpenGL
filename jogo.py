from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame

from JogadorClass import Jogador
from AtiradorClass import Atirador
from RazanteClass import Razante
from TelaClass import Tela

from random import randint

def loadImage(image):

    textureSurface = pygame.image.load(image)
    textureData = pygame.image.tostring(textureSurface, "RGB", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB,GL_UNSIGNED_BYTE, textureData)

    return texture

#texturas
t0 = loadImage("./Texturas/coracao.png")

w,h=1000,1000

#Número de inimigos para atirar, iniciando do indice 0
numAtiradores = 14

#porcentagem de chance de algum inimigo ou razante ativar por ciclo
agressividade = 5

#jogador variavel global
j = Jogador()

#Tela que controla em qual estagio o jogo está, além do background e sprites na tela
t = Tela(j,t0)

#inimigos atiradores
a00 = Atirador(875,925)
a01 = Atirador(775,925)
a02 = Atirador(675,925)
a03 = Atirador(575,925)
a04 = Atirador(475,925)
a10 = Atirador(875,825)
a11 = Atirador(775,825)
a12 = Atirador(675,825)
a13 = Atirador(575,825)
a14 = Atirador(475,825)
a20 = Atirador(875,725)
a21 = Atirador(775,725)
a22 = Atirador(675,725)
a23 = Atirador(575,725)
a24 = Atirador(475,725)
alist = [a00,a01,a02,a03,a04,a10,a11,a12,a13,a14,a20,a21,a22,a23,a24]

#inimigos razantes
r00 = Razante(975,925)
r01 = Razante(375,925)
r10 = Razante(975,825)
r11 = Razante(375,825)
r20 = Razante(975,725)
r21 = Razante(375,725)
rlist = [r00,r01,r10,r11,r20,r21]

#lista de todos os inimigos juntos
elist = alist + rlist

etiros = []


def quadrado(posx,posy,h,l):
    glColor3f(0.0, 1.0, 0.0)
    glPushMatrix()
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(posx-l/2, posy-h/2)
    glVertex2f(posx+l/2, posy-h/2)
    glVertex2f(posx+l/2, posy+h/2)
    glVertex2f(posx-l/2, posy+h/2)
    glEnd()
    glPopMatrix()

def quadradoTextura(posx,posy,h,l,textura):
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D,textura)
    glPushMatrix()
    glBegin(GL_TRIANGLE_FAN)
    glTexCoord2f(0,0)
    glVertex2f(posx-l/2, posy-h/2)
    glTexCoord2f(1,0)
    glVertex2f(posx+l/2, posy-h/2)
    glTexCoord2f(1,1)
    glVertex2f(posx+l/2, posy+h/2)
    glTexCoord2f(0,1)
    glVertex2f(posx-l/2, posy+h/2)
    glEnd()
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def tiroJogador():
    j.moverTiro()

def moverInimigos():
    #mover para a direita se encostar na esquerda
    if r01.getX() < 25:
        for x in elist:
            x.setDir(1) 
            x.setY(x.getY()-100) #descer 100px
    #mover para a esquerda se encostar na direita
    elif r00.getX() > 975:
        for x in elist:
            x.setDir(-1)
            x.setY(x.getY()-100) #descer 100px
    for x in elist:
        x.movimentar()
    #movimentos oscilantes para cima e para baixo(não implementados ainda)


def moverJogador():
    #movimentos do teclado
    if j.getA():
        j.moverT(-1)
    elif j.getD():
        j.moverT(1)

def checarColisaoPlayer():
    #checa se o tiro foi atirado, se sim checa sua colisão com cada inimigo
    for x in j.getTiros():
        if x.atirado == True:
            for y in elist:
                if checarColisaoRetangulos(y.getX(),y.getY(),y.getL(),y.getH(),x.getX(),x.getY(),10,50) and y.getVivo():
                    y.setVivo(False)
                    x.setAtirado(False)

def checarColisaoTiros():
    for x in etiros:
        if x.atirado == True:
            if checarColisaoRetangulos(x.getX(),x.getY(),10,50,j.getX(),j.getY(),j.getL(),j.getH()):
                j.setVidas(j.getVidas()-1)
                x.setAtirado(False)
                t.atualizarSprites()

def checarColisaoRetangulos(ax,ay,al,ah,bx,by,bl,bh):
    colisaoX = False
    if ax + al/2 >= bx - bl/2 and bx + bl/2 >= ax - al/2:
        colisaoX = True
    colisaoY = False
    if ay + ah/2 >= by - bh/2 and by + bh/2 >= ay - ah/2:
        colisaoY = True
    return colisaoX and colisaoY

def tiroInimigos():
    global etiros,alist
    #chance para um inimigo atirar a cada atualização
    temp1 = randint(0,100)
    #porcentagem de chance
    if temp1 < agressividade:
        temp2 = randint(0,numAtiradores) #randomizar o inimigo que ira atirar
        temp3 = 0 #contar até chegar o inimigo que ira atirar
        for x in alist:
            if temp3 != temp2:
                temp3 += 1
            elif x.getTiro().getAtirado() == False and x.getVivo() == True:
                x.atirar()
                #    Alguns tiros sao colocados duas vezes na lista, eles se movimentam duas vezes por causa disso,
                # mas vou chamar isso de feature ao invés de bug porque gostei da diversidade, mesmo podendo arrumar
                # retirando os duplicados antes do passo de move-los
                etiros.append(x.getTiro())
                break
    #mover os tiros
    for x in etiros:
        #se o tiro tiver acertado ou passado do limite, retirar da lista
        if x.getAtirado() == False:
            etiros.remove(x)
        else:
            x.mover()

def redimensiona(width,height):
    #manter aspect ratio
    global w,h
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, w, 0, h, -1, 1)

    razaoAspectoJanela = (width)/height
    razaoAspectoMundo = (w)/h
    if razaoAspectoJanela < razaoAspectoMundo:
        hViewport = width / razaoAspectoMundo
        yViewport = (height - hViewport)/2
        glViewport(0, yViewport, width, hViewport)
    
    elif razaoAspectoJanela > razaoAspectoMundo:
        wViewport = (height) * razaoAspectoMundo
        xViewport = (width - wViewport)/2
        glViewport(xViewport, 0, wViewport, height)
    else:
        glViewport(0, 0, width, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def iterate():
    global w,h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def desenhaCena():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #desenha jogador
    quadrado(j.getX(),j.getY(),j.getL(),j.getH())
    #desenha inimigos
    for x in elist:
        if x.getVivo() == True:
            quadrado(x.getX(),x.getY(),x.getL(),x.getH())
    #desenha tiro jogador
    for x in j.getTiros():
        if x.getAtirado():
            quadrado(x.getX(),x.getY(),50,10)
    #desenha tiros inimigos
    for x in etiros:
        quadrado(x.getX(),x.getY(),50,10)
    #desenha tela
    for x in t.getSprites():
        quadradoTextura(x.getX(),x.getY(),x.getL(),x.getH(),0)
    glutSwapBuffers()

def atualizaCena(periodo):

    if t.getEstagio() == "jogo":
        #atualizar tiro jogador
        tiroJogador()

        #movimentos
        moverInimigos()
        moverJogador()

        #ações dos inimigos
        tiroInimigos()


        #checar a colisão dos tiros do player
        checarColisaoPlayer()

        #checar a colisão dos tiros inimigos
        checarColisaoTiros()

        if j.getVidas() == 0:
            t.setEstagio("game over")

    glutPostRedisplay()
    glutTimerFunc(periodo,atualizaCena,periodo)

def inicializar():
    glEnable(GL_BLEND )
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def teclado(key,x,y):
    if key == b'd':
        j.setD(True)
    elif key == b'a':
        j.setA(True)
    elif key == b' ':
        j.atirar()
        

def tecladoUp(key,x,y):
    if key == b'd':
        j.setD(False)
    elif key == b'a':
        j.setA(False)

def movimentoMouse(x,y):
    if t.getEstagio() == "jogo":
        j.moverM(x,y)

def clickMouse(key,state,x,y):
    if key == GLUT_LEFT_BUTTON and state == GLUT_DOWN and t.getEstagio() == "jogo":
        j.atirar()


if __name__ == "__main__":

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)

    wind = glutCreateWindow("jojo do zilla")
    inicializar()

    glutDisplayFunc(desenhaCena)
    #glutReshapeFunc(redimensiona) #não funcionando
    glutKeyboardFunc(teclado)
    glutKeyboardUpFunc(tecladoUp)
    glutPassiveMotionFunc(movimentoMouse)
    glutMouseFunc(clickMouse)
    glutTimerFunc(0,atualizaCena,33)

    glutMainLoop()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, cos, sin, sqrt
px,py=0,0
L=200
angle=0
dangle=5
bucketx,buckety=6,-100
lhand=-20
rhand=10
maxang=30
inc=2
inc2=2
dy=2
ropex,ropey=30,-70
ropexinc=-1
ropeyinc=-1
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(4)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_circle(x, y, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 10):
        theta = i * pi / 180.0
        glVertex2f(x + r * cos(theta), y + r * sin(theta))
    glEnd()
def draw_lines(x,y,r):
    glPushMatrix()
    glTranslatef(x,y,0)
    for i in range(4):
        glRotatef(i*90,0,0,1)
        glBegin(GL_LINES)
        glVertex2f(0,r)
        glVertex2f(0,0)
        glEnd()
    glPopMatrix()
def display():
    global angle,bucketx,buckety,lhand,rhand,ropex,ropey
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #man
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(px,py)
    glVertex2f(px,-L)
    glEnd()
    draw_circle(px,py,30)
    glBegin(GL_LINES)
    glVertex2f(px,-L)
    glVertex2f(10,-250)
    glEnd()
    draw_circle(px,py,20)
    glBegin(GL_LINES)
    glVertex2f(px,-L)
    glVertex2f(-10,-250)
    glEnd()
    #lhand
    glPushMatrix()
    glTranslatef(px,-L/2,0)
    glRotatef(lhand,0,0,1)
    glTranslatef(-px,L/2,0)
    glBegin(GL_LINES)
    glVertex2f(30,-60)
    glVertex2f(px,-L/2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(50,-20)
    glVertex2f(30,-60)
    glEnd()
    glPopMatrix()
    #rhand
    glPushMatrix()
    glTranslatef(px,-L/2,0)
    glRotatef(rhand,0,0,1)
    glTranslatef(-px,L/2,0)
    glBegin(GL_LINES)
    glVertex2f(30,-60)
    glVertex2f(px,-L/2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(50,-10)
    glVertex2f(30,-60)
    glEnd()
    glPopMatrix()
    #rope
    glColor3f(1,0,1)
    glBegin(GL_LINES)
    glVertex2f(150,-150)
    glVertex2f(150,0)
    glEnd()
    glColor3f(1,0,1)
    glBegin(GL_LINES)
    glVertex2f(ropex,ropey)
    glVertex2f(150,0)
    glEnd()
    #Bucket
    glPushMatrix()
    glTranslatef(bucketx,buckety,0)
    glColor3f(0.5,0.35,0.05)
    glBegin(GL_QUADS)
    glVertex2f(130,-150)
    glVertex2f(170,-150)
    glVertex2f(180,-100)
    glVertex2f(120,-100)
    glEnd()
    glPopMatrix()
    #well
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex2f(80,-250)
    glVertex2f(220,-250)
    glVertex2f(220,-90)
    glVertex2f(80,-90)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(220,-100)
    glVertex2f(220,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(80,-100)
    glVertex2f(80,0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(220,0)
    glVertex2f(80,0)
    glEnd()
    #pulley
    glPushMatrix()
    glColor3f(1,0,0)
    draw_circle(150,0,20)
    glColor3f(1,1,1)
    glTranslatef(150,0,0)
    glRotatef(angle,0,0,1)
    glTranslatef(-150,0,0)
    draw_lines(150,0,20)
    glPopMatrix()
    
    glutSwapBuffers()

def update(v):
    global angle,dangle,buckety,bucketx,lhand,inc,rhand,inc2,maxang,dy,ropex,ropey,ropexinc,ropeyinc
    angle+=dangle
    if angle>=360:
        angle-=360
    buckety+=dy
    ropex+=ropexinc
    ropey+=ropeyinc
    if buckety>=70:
        buckety=70
        dy*=-1
        ropexinc*=-1
        ropeyinc*=-1 
        dangle*=-1   
    if buckety<=-100:
        dy*=-1   
        ropexinc*=-1
        ropeyinc*=-1
        dangle*=-1
    lhand+=inc
    if lhand>=maxang or lhand<=-maxang:
        inc*=-1
    rhand+=inc2
    if rhand>=maxang or rhand<=-maxang:
        inc2*=-1    
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Pendulum smashing a ball (fixed)")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()
main()

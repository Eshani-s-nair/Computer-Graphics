from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, sin, cos

px, py = 0, 100      
L = 100   
xmax=500
ymax=500          
tx,ty=1,1       
llx,lly,rlx,rly=-15,-110,15,-110
inc=0.2
def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)

def draw_circle(x, y, r, num_segments=50):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        t = 2 * pi * i / num_segments
        glVertex2f(x + r * cos(t), y + r * sin(t))
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(px, py, 0)               
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0, -L)                
    glEnd()
    draw_circle(0, 0, 10)
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(0, -L)
    glVertex2f(llx, lly)                
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,-L)
    glVertex2f(rlx, rly)                
    glEnd()
    glPopMatrix()
    glBegin(GL_LINES)
    glVertex2f(250,250)
    glVertex2f(0,0)                
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(250,250)
    glVertex2f(500,0)                
    glEnd()
    glutSwapBuffers()

def update(v):
    global tx,ty ,px,py,xmax,ymax,llx,lly,rlx,rly,inc
    px+=tx
    py+=ty
    llx+=inc
    rlx+=inc


    if llx<-20 or rlx>20:
        llx,rlx=-15,15,

    if px==250:
        ty*=-1
    if px>xmax or py>ymax :
        return
    glutPostRedisplay()
    glutTimerFunc(16,update,0)





def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Pendulum Animation (Rotatef)")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

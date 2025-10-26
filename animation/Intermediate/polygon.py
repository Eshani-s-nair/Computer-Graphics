#rotation and translation
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi

xc,yc=200,233  
xmin, xmax = 0, 800
ymin, ymax = 0, 800
angle=30
dangle=5
x_value=50
dx=3

def init():
    glClearColor(0, 0, 0, 1)
    glColor3f(1.0,1.0,1.0)
    glPointSize(4)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xmin, xmax, ymin, ymax)

def draw():
    global angle,x_value
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(x_value,0,0)
    glTranslatef(xc,yc,0)
    glRotatef(angle,0,0,1)
    glTranslatef(-xc,-yc,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(200,300)
    glVertex2f(150,200)
    glVertex2f(250,200)
    glEnd()
    glPopMatrix()
    glutSwapBuffers()

def update(v):
    global angle,x_value,dx
    angle+=dangle
    x_value+=dx
    if angle>=360:
        angle-=360
    if x_value>=750:
        dx*=-1

    glutPostRedisplay()
    glutTimerFunc(16,update,0)    


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bouncing Ball (Diagonal)")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

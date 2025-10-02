from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x1,y1,x2,y2=100,100,300,200
tx,ty=50,50

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glEnd()
    x1_t, y1_t, x2_t, y2_t = translate(x1,y1,x2,y2)
    print("Translated Line Coordinates: ", x1_t, y1_t, x2_t, y2_t)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1_t,y1_t)
    glVertex2i(x2_t,y2_t)
    glEnd()
    glFlush()
def translate(x1,y1,x2,y2):
    x1_translated=x1+tx
    y1_translated=y1+ty
    x2_translated=x2+tx
    y2_translated=y2+ty
    return x1_translated,y1_translated,x2_translated,y2_translated

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Line Translation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()

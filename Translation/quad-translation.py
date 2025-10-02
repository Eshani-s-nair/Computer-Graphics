#translation of a shape (quadrilateral) wrt origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x1,y1,x2,y2=100,100,300,200
x3,y3,x4,y4=300,300,100,300
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
    glBegin(GL_LINE_LOOP)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glVertex2i(x3,y3)
    glVertex2i(x4,y4)
    glEnd()
    x1_t, y1_t, x2_t, y2_t, x3_t, y3_t, x4_t, y4_t = translate(x1,y1,x2,y2,x3,y3,x4,y4)
    print("Translated Shape Coordinates: ", x1_t, y1_t, x2_t, y2_t, x3_t, y3_t, x4_t, y4_t)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2i(x1_t,y1_t)
    glVertex2i(x2_t,y2_t)
    glVertex2i(x3_t,y3_t)
    glVertex2i(x4_t,y4_t)
    glEnd()
    glFlush()
def translate(x1,y1,x2,y2,x3,y3,x4,y4):
    x1_translated=x1+tx
    y1_translated=y1+ty
    x2_translated=x2+tx
    y2_translated=y2+ty
    x3_translated=x3+tx
    y3_translated=y3+ty
    x4_translated=x4+tx
    y4_translated=y4+ty
    return x1_translated,y1_translated,x2_translated,y2_translated,x3_translated,y3_translated,x4_translated,y4_translated
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Shape Translation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()      
#rotation wrt origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x1,y1,x2,y2=100,0,300,0
angle=45
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
    x1_r, y1_r, x2_r, y2_r = rotate(x1,y1,x2,y2)
    print("Rotated Line Coordinates: ", x1_r, y1_r, x2_r, y2_r)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1_r,y1_r)
    glVertex2i(x2_r,y2_r)
    glEnd()
    glFlush()
def rotate(x1,y1,x2,y2):
    x1_rotated= x1 * math.cos(math.radians(angle)) - y1 * math.sin(math.radians(angle))
    y1_rotated= x1 * math.sin(math.radians(angle)) + y1 * math.cos(math.radians(angle))
    x2_rotated= x2 * math.cos(math.radians(angle)) - y2 * math.sin(math.radians(angle))
    y2_rotated= x2 * math.sin(math.radians(angle)) + y2 * math.cos(math.radians(angle))
    return int(x1_rotated),int(y1_rotated),int(x2_rotated),int(y2_rotated)
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Line Rotation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()    
#rotation of quadrilateral wrt origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x1,y1,x2,y2=100,100,300,200
x3,y3,x4,y4=300,300,100,300
angle=20
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
    glBegin(GL_QUADS)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glVertex2i(x3,y3)
    glVertex2i(x4,y4)
    glEnd()
    x1_r, y1_r, x2_r, y2_r, x3_r, y3_r, x4_r, y4_r = rotate(x1,y1,x2,y2,x3,y3,x4,y4)
    print("Rotated Shape Coordinates: ", x1_r, y1_r, x2_r, y2_r, x3_r, y3_r, x4_r, y4_r)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_QUADS)
    glVertex2i(x1_r,y1_r)
    glVertex2i(x2_r,y2_r)
    glVertex2i(x3_r,y3_r)
    glVertex2i(x4_r,y4_r)
    glEnd()
    glFlush()
def rotate(x1,y1,x2,y2,x3,y3,x4,y4):
    x1_rotated= x1 * math.cos(math.radians(angle)) - y1 * math.sin(math.radians(angle))
    y1_rotated= x1 * math.sin(math.radians(angle)) + y1 * math.cos(math.radians(angle))
    x2_rotated= x2 * math.cos(math.radians(angle)) - y2 * math.sin(math.radians(angle))
    y2_rotated= x2 * math.sin(math.radians(angle)) + y2 * math.cos(math.radians(angle))
    x3_rotated= x3 * math.cos(math.radians(angle)) - y3 * math.sin(math.radians(angle))
    y3_rotated= x3 * math.sin(math.radians(angle)) + y3 * math.cos(math.radians(angle))
    x4_rotated= x4 * math.cos(math.radians(angle)) - y4 * math.sin(math.radians(angle))
    y4_rotated= x4 * math.sin(math.radians(angle)) + y4 * math.cos(math.radians(angle))
    return int(x1_rotated),int(y1_rotated),int(x2_rotated),int(y2_rotated),int(x3_rotated),int(y3_rotated),int(x4_rotated),int(y4_rotated)      
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Quadrilateral Rotation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()      
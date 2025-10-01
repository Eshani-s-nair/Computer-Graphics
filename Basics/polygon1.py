#user defined no of edges
from OpenGL.GL import *
from OpenGL.GLUT import *       
from OpenGL.GLU import *
import math
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)  
def display():
    glClear(GL_COLOR_BUFFER_BIT)  
    n = int(input("Enter number of edges: "))
    r = 150
    cx, cy = 250, 250  
    glBegin(GL_POLYGON)
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        glVertex2i(int(x), int(y))
    glEnd()
    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Polygon Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()        
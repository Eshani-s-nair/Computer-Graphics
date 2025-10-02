#bouncing ball along x direction
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi
import sys
x, y = 0, 0          
dx =2   
radius = 20       
xmin, xmax = -200, 200
ymin, ymax = -200, 200
def init():
    glClearColor(0, 0, 0, 1)         
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xmin, xmax, ymin, ymax)
def display():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)  
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for angle in range(0, 361, 10):
        glVertex2f(x + radius * cos(angle * pi / 180), y + radius * sin(angle * pi / 180))
    glEnd()
    glutSwapBuffers()  
def update(v):
    global x, y, dx, dy
    x += dx
    if x + radius >= xmax or x - radius <= xmin:
        dx = -dx
    glutPostRedisplay()            
    glutTimerFunc(16, update, 0)  
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB) 
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bouncing Ball")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0) 
    glutMainLoop()
main()

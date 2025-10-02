from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi
import sys

# Circle parameters
x_center, y_center = 0, 0
radius = 30
scale_factor = 1.0
scale_step = 0.01  

def init():
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200,200,-200,200)

def display():
    global scale_factor
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,1)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x_center, y_center)
    for angle in range(0, 361, 10):
        glVertex2f(x_center + radius * scale_factor * cos(angle * pi / 180),
                   y_center + radius * scale_factor * sin(angle * pi / 180))
    glEnd()
    glutSwapBuffers()

def update(v):
    global scale_factor, scale_step
    scale_factor += scale_step
    if scale_factor >= 2.0 or scale_factor <= 0.5:
        scale_step = -scale_step
    glutPostRedisplay()
    glutTimerFunc(16, update, 0) 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Scaling Circle")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

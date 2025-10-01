#circle drawing using triangle fan
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
def draw_circle(xc, yc, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(xc, yc)  # Center of circle
    num_segments = 360
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        x = xc + r * math.cos(theta)
        y = yc + r * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
def display():
    glClear(GL_COLOR_BUFFER_BIT)  
    draw_circle(250, 250, 100)
    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Circle Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()            
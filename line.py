from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2i(100, 100)
    glVertex2i(400, 400)
    glEnd()
    glFlush()
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Line Example")    
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()    
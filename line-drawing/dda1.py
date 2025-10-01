#line drawing using DDA algorithm with user input
from OpenGL.GL import *
from OpenGL.GLU import *    
from OpenGL.GLUT import *
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)        
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()    
    gluOrtho2D(0, 500, 0, 500)
def drawDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    glBegin(GL_POINTS)
    for i in range(steps):
        glVertex2i(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    drawDDA(x1, y1, x2, y2)
    glFlush()   
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"DDA Line Drawing Algorithm with User Input")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()           
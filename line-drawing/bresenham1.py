#line drawing using bresenham's algorithm with user input
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
def drawBresenham(x1, y1, x2, y2):
    if x1>x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    dx = x2 - x1
    dy = y2 - y1
    x,y=x1,y1
    sx = 1 if dx > 0 else -1
    sy = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx >= dy:
        p=2 * dy - dx
        for i in range(dx):
            glVertex2i(x, y)
            x += sx
            if p < 0:
                p += 2 * dy
            else:
                y += sy
                p += 2 * dy - 2 * dx
    else:
        p=2 * dx - dy
        for i in range(dy):
            glVertex2i(x, y)
            y += sy
            if p < 0:
                p += 2 * dx
            else:
                x += sx
                p += 2 * dx - 2 * dy
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    glBegin(GL_POINTS)
    drawBresenham(x1, y1, x2, y2)
    glEnd()
    glFlush()              
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bresenham's Line Drawing Algorithm with User Input")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()              
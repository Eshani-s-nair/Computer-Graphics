#circle drawing using bresenham's algorithm with predefined points
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
def drawBresenhamCircle(xc,yc,r):
    x=0
    y=r
    d =3-2*r
    plotCirclePoints(xc,yc,x,y)
    while x<=y:
        if d<0:
            d=d+4*x+6
        else:
            d=d+4*(x-y)+10
            y=y-1
        x=x+1
        plotCirclePoints(xc,yc,x,y)
def plotCirclePoints(xc,yc,x,y):
    glBegin(GL_POINTS)
    glVertex2i(xc+x,yc+y)
    glVertex2i(xc-x,yc+y)
    glVertex2i(xc+x,yc-y)
    glVertex2i(xc-x,yc-y)
    glVertex2i(xc+y,yc+x)
    glVertex2i(xc-y,yc+x)
    glVertex2i(xc+y,yc-x)
    glVertex2i(xc-y,yc-x)
    glEnd()
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawBresenhamCircle(250,250,100)
    glFlush()           
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Bresenham's Circle Drawing Algorithm")
    init()
    glutDisplayFunc(display)
    glutMainLoop()      
main()                    
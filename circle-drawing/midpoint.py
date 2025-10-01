#circle draeing using midpoint algorithm
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
def plotpoints(xc,yc,x,y):
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
def draw_circle(xc,yc,r):
    x=0
    y=r
    d=1-r
    plotpoints(xc,yc,x,y)
    while(x<y):
        if(d<0):
            d=d+2*x+3
            x=x+1
        else:
            d=d+2*x-2*y+5
            x=x+1
            y=y-1
        plotpoints(xc,yc,x,y)   
def display():
    glClear(GL_COLOR_BUFFER_BIT)  
    draw_circle(250,250,100)
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
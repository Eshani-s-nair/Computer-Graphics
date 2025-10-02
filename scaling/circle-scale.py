#scaling circle wrt origin (symmetric scaling)
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x_c,y_c=200,200
r=50
s=2
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(0.0,1.0,0.0,0.3)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2i(x_c,y_c)
    for angle in range(0,361,10):
        x= x_c + r * math.cos(math.radians(angle))
        y= y_c + r * math.sin(math.radians(angle))
        glVertex2f(x,y)
    glEnd()
    n_r= scale(r,s)
    print("Scaled Circle Center Coordinates: ", x_c, y_c)
    glColor4f(1.0,0.0,0.0,0.5)  
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x_c,y_c)
    for angle in range(0,361,10):
        x_s= x_c + n_r * math.cos(math.radians(angle))
        y_s= y_c + n_r * math.sin(math.radians(angle))
        glVertex2f(x_s,y_s)
    glEnd()
    glFlush()
def scale(r,s):
    return r*s
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Circle Scaling Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()    
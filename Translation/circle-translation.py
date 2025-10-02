#translation of shape (circle)
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x_c,y_c=200,200
r=50
tx,ty=50,50
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2i(x_c,y_c)
    for angle in range(0,361,10):
        x= x_c + r * math.cos(math.radians(angle))
        y= y_c + r * math.sin(math.radians(angle))
        glVertex2f(x,y)
    glEnd()
    x_c_t, y_c_t = translate(x_c,y_c)
    print("Translated Circle Center Coordinates: ", x_c_t, y_c_t)
    glColor3f(1.0,0.0,0.0)  
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x_c_t,y_c_t)
    for angle in range(0,361,10):
        x_t= x_c_t + r * math.cos(math.radians(angle))
        y_t= y_c_t + r * math.sin(math.radians(angle))
        glVertex2f(x_t,y_t)
    glEnd()
    glFlush()   
def translate(x_c,y_c):
    x_c_translated=x_c+tx
    y_c_translated=y_c+ty
    return x_c_translated,y_c_translated
def main():         
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Circle Translation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
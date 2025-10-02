#line rotation wrt to a reference point 
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x1,y1,x2,y2=100,0,300,0
angle=45
xr,yr=100,0
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
    glBegin(GL_LINES)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glEnd()
    x1_r, y1_r, x2_r, y2_r = rotate(x1,y1,x2,y2)
    print("Rotated Line Coordinates: ", x1_r, y1_r, x2_r, y2_r)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1_r,y1_r)
    glVertex2i(x2_r,y2_r)
    glEnd()
    glFlush()
def rotate(x1,y1,x2,y2):
    x1_shifted, y1_shifted = x1 - xr, y1 - yr
    x2_shifted, y2_shifted = x2 - xr, y2 - yr
    x1_rotated= x1_shifted * math.cos(math.radians(angle)) - y1_shifted * math.sin(math.radians(angle))
    y1_rotated= x1_shifted * math.sin(math.radians(angle)) + y1_shifted * math.cos(math.radians(angle))
    x2_rotated= x2_shifted * math.cos(math.radians(angle)) - y2_shifted * math.sin(math.radians(angle))
    y2_rotated= x2_shifted * math.sin(math.radians(angle)) + y2_shifted * math.cos(math.radians(angle))
    x1_final, y1_final = int(x1_rotated + xr), int(y1_rotated + yr)
    x2_final, y2_final = int(x2_rotated + xr), int(y2_rotated + yr)
    return x1_final,y1_final,x2_final,y2_final
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Line Rotation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()        
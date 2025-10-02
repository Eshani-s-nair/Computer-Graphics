#quadrialteral rotation wrt reference point
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
x1,y1,x2,y2=100,100,300,200
x3,y3,x4,y4=300,300,100,300
angle=20
xr,yr=100,100
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
    glBegin(GL_QUADS)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glVertex2i(x3,y3)
    glVertex2i(x4,y4)
    glEnd()
    x1_r, y1_r, x2_r, y2_r, x3_r, y3_r, x4_r, y4_r = rotate(x1,y1,x2,y2,x3,y3,x4,y4)
    print("Rotated Shape Coordinates: ", x1_r, y1_r, x2_r, y2_r, x3_r, y3_r, x4_r, y4_r)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_QUADS)
    glVertex2i(x1_r,y1_r)
    glVertex2i(x2_r,y2_r)
    glVertex2i(x3_r,y3_r)
    glVertex2i(x4_r,y4_r)
    glEnd()
    glFlush()
def rotate(x1,y1,x2,y2,x3,y3,x4,y4):    
    x1_shifted, y1_shifted = x1 - xr, y1 - yr
    x2_shifted, y2_shifted = x2 - xr, y2 - yr
    x3_shifted, y3_shifted = x3 - xr, y3 - yr
    x4_shifted, y4_shifted = x4 - xr, y4 - yr
    x1_rotated= x1_shifted * math.cos(math.radians(angle)) - y1_shifted * math.sin(math.radians(angle))
    y1_rotated= x1_shifted * math.sin(math.radians(angle)) + y1_shifted * math.cos(math.radians(angle))
    x2_rotated= x2_shifted * math.cos(math.radians(angle)) - y2_shifted * math.sin(math.radians(angle))
    y2_rotated= x2_shifted * math.sin(math.radians(angle)) + y2_shifted * math.cos(math.radians(angle))
    x3_rotated= x3_shifted * math.cos(math.radians(angle)) - y3_shifted * math.sin(math.radians(angle))
    y3_rotated= x3_shifted * math.sin(math.radians(angle)) + y3_shifted * math.cos(math.radians(angle))
    x4_rotated= x4_shifted * math.cos(math.radians(angle)) - y4_shifted * math.sin(math.radians(angle))
    y4_rotated= x4_shifted * math.sin(math.radians(angle)) + y4_shifted * math.cos(math.radians(angle))
    x1_final, y1_final = int(x1_rotated + xr), int(y1_rotated + yr)
    x2_final, y2_final = int(x2_rotated + xr), int(y2_rotated + yr)
    x3_final, y3_final = int(x3_rotated + xr), int(y3_rotated + yr)
    x4_final, y4_final = int(x4_rotated + xr), int(y4_rotated + yr)
    return x1_final,y1_final,x2_final,y2_final,x3_final,y3_final,x4_final,y4_final
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Quadrilateral Rotation Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
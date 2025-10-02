#quadrilateral scaling wrt a reference point
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x1,y1,x2,y2=100,100,300,200
x3,y3,x4,y4=300,300,100,300
sx,sy=0.5,0.5
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
    x1_s, y1_s, x2_s, y2_s, x3_s, y3_s, x4_s, y4_s = scale(x1,y1,x2,y2,x3,y3,x4,y4)
    print("Scaled Shape Coordinates: ", x1_s, y1_s, x2_s, y2_s, x3_s, y3_s, x4_s, y4_s)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_QUADS)
    glVertex2i(x1_s,y1_s)
    glVertex2i(x2_s,y2_s)
    glVertex2i(x3_s,y3_s)
    glVertex2i(x4_s,y4_s)
    glEnd()
    glFlush()
def scale(x1,y1,x2,y2,x3,y3,x4,y4):
    x1_shifted, y1_shifted = x1 - xr, y1 - yr
    x2_shifted, y2_shifted = x2 - xr, y2 - yr
    x3_shifted, y3_shifted = x3 - xr, y3 - yr
    x4_shifted, y4_shifted = x4 - xr, y4 - yr
    x1_scaled=x1_shifted*sx
    y1_scaled=y1_shifted*sy
    x2_scaled=x2_shifted*sx
    y2_scaled=y2_shifted*sy
    x3_scaled=x3_shifted*sx
    y3_scaled=y3_shifted*sy
    x4_scaled=x4_shifted*sx
    y4_scaled=y4_shifted*sy
    x1_final, y1_final = int(x1_scaled + xr), int(y1_scaled + yr)
    x2_final, y2_final = int(x2_scaled + xr), int(y2_scaled + yr)
    x3_final, y3_final = int(x3_scaled + xr), int(y3_scaled + yr)
    x4_final, y4_final = int(x4_scaled + xr), int(y4_scaled + yr)
    return x1_final,y1_final,x2_final,y2_final,x3_final,y3_final,x4_final,y4_final
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Quadrilateral Scaling Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
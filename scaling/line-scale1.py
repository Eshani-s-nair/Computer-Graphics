#line scaling wrt to a reference point
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x1,y1,x2,y2=50,100,200,300
sx,sy=2,2
xr,yr=20,100
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glLineWidth(3.0) 
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
    x1_s, y1_s, x2_s, y2_s = scale(x1,y1,x2,y2)
    print("Scaled Line Coordinates: ", x1_s, y1_s, x2_s, y2_s)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1_s,y1_s)
    glVertex2i(x2_s,y2_s)
    glEnd()
    glFlush()
def scale(x1,y1,x2,y2):
    x1_shifted, y1_shifted = x1 - xr, y1 - yr
    x2_shifted, y2_shifted = x2 - xr, y2 - yr
    x1_scaled=x1_shifted*sx
    y1_scaled=y1_shifted*sy
    x2_scaled=x2_shifted*sx
    y2_scaled=y2_shifted*sy
    x1_final, y1_final = int(x1_scaled + xr), int(y1_scaled + yr)
    x2_final, y2_final = int(x2_scaled + xr), int(y2_scaled + yr)
    return x1_final,y1_final,x2_final,y2_final
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Line Scaling Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
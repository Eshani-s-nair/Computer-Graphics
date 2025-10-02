#circle scaling wrt reference point
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
xc,yc=250,250
r=100
sx,sy=1.5,1.5
xr,yr=100,150
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(3.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor4f(0.0,1.0,0.0,0.5)
    draw_circle(xc,yc,r)
    xc_s, yc_s, r_s = scale(xc,yc,r)
    print("Scaled Circle Center and Radius: ", xc_s, yc_s, r_s)
    glColor4f(1.0,0.0,0.0,0.5)
    draw_circle(xc_s,yc_s,r_s)
    glFlush()
def draw_circle(xc,yc,r):
    glBegin(GL_TRIANGLE_FAN)
    for angle in range(0,361,10):
        x= xc + r * math.cos(math.radians(angle))
        y= yc + r * math.sin(math.radians(angle))
        glVertex2f(x,y)
    glEnd()
def scale(xc,yc,r):
    xc_shifted, yc_shifted = xc - xr, yc - yr
    xc_scaled=xc_shifted*sx
    yc_scaled=yc_shifted*sy
    r_scaled=r*sx
    xc_final, yc_final = int(xc_scaled + xr), int(yc_scaled + yr)
    return xc_final,yc_final,int(r_scaled)
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
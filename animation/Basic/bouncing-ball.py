from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi


x, y = 0, 300         
dx, dy = 0.8, 0        
radius = 20 
gravity = -0.15        
floor_y = radius      
damping = 0.8          
xmin, xmax = 0, 500
ymin, ymax = 0, 500

def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xmin, xmax, ymin, ymax)

def display():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for angle in range(0, 361, 10):
        glVertex2f(x + radius * cos(angle * pi / 180), y + radius * sin(angle * pi / 180))
    glEnd()
    glutSwapBuffers()

def update(v):
    global x, y, dx, dy, gravity, floor_y
    x += dx
    dy += gravity
    y += dy
    if y < floor_y:
        y = floor_y
        dy = -dy * damping
        if abs(dy)<0.1:
            dy,dx=0,0
            y=floor_y
            return
    if x > xmax - radius:
        x = radius
        y = 400
        dy = 0

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bouncing Ball (Diagonal)")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

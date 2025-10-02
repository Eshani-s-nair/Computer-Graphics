from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sin, cos, pi
px, py = 0, 100   
L = 100               
theta = 30          
dtheta = 1            
max_angle = 60       
direction = 1         # 1 for right, -1 for left
def init():
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200,200,-200,200)
def draw_circle(x, y, r, num_segments=50):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        t = 2*pi*i/num_segments
        glVertex2f(x + r*cos(t), y + r*sin(t))
    glEnd()
def display():
    global theta
    glClear(GL_COLOR_BUFFER_BIT)
    rad = theta * pi/180
    x = px + L * sin(rad)
    y = py - L * cos(rad)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    glVertex2f(px, py)
    glVertex2f(x, y)
    glEnd()
    glColor3f(1,0,0)
    draw_circle(x, y, 10)
    glColor3f(0,1,0)
    draw_circle(px, py, 5)
    glutSwapBuffers()
def update(v):
    global theta, direction
    theta += dtheta * direction
    if theta >= max_angle or theta <= -max_angle:
        direction *= -1   
    glutPostRedisplay()
    glutTimerFunc(16, update, 0) 

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Pendulum Animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

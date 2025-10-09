from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, sin, cos

px, py = 0, 100      
L = 100             
theta = 0           
dtheta = 1            
max_angle = 60        
direction = 1       

def init():
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)

def draw_circle(x, y, r, num_segments=50):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        t = 2 * pi * i / num_segments
        glVertex2f(x + r * cos(t), y + r * sin(t))
    glEnd()

def display():
    global theta
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPushMatrix()
    glTranslatef(px, py, 0)           
    glRotatef(theta, 0, 0, 1)         

    
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0, -L)                
    glEnd()

    glColor3f(1, 0, 0)
    draw_circle(0, -L, 10)

    glPopMatrix()

    glColor3f(0, 1, 0)
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
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Pendulum Animation (Rotatef)")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

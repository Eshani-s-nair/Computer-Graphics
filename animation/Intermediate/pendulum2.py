#pendulum colliding with a ball and losing energy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import pi, cos, sin, sqrt


L = 200
angle = 0
incang = 2
maxangle = 60
direction = 1
radius = 25
damping = 0.8

px,py=0,0
bx, by = 495.0, -180.0
bradius = 15
speed = 4.0
collid = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(4)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_circle(x, y, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 10):
        theta = i * pi / 180.0
        glVertex2f(x + r * cos(theta), y + r * sin(theta))
    glEnd()

def display():
    global angle, bx, by
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    draw_circle(bx, by, bradius)
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(px, py)
    glVertex2f(px, -L)
    glEnd()
    glColor3f(1.0, 0.0, 0.0)
    draw_circle(px, -L, radius)
    glPopMatrix()
    glColor3f(1.0, 0.0, 1.0)
    draw_circle(0.0, 0.0, 5.0)

    glutSwapBuffers()

def update(v):
    global angle, incang, direction, bx, by, speed, collid, maxangle,damping
    
    angle += incang * direction    
    bx -= speed
    if angle >= maxangle:
            angle = maxangle
            direction = -1
        
    elif angle <= -maxangle:
        angle = -maxangle
        direction = 1

    pend_x = L * sin(angle * pi / 180.0)
    pend_y = -L * cos(angle * pi / 180.0)
    dist = sqrt((bx - pend_x)**2 + (by - pend_y)**2)
    if collid == 0:
        if dist <= (radius + bradius):
            collid = 1
            speed = -speed * 0.99
    else:
        bx -= speed
        speed *= 0.98
        maxangle *= 0.99
        if abs(speed) < 0.01:
            speed = 0.0
    if abs(maxangle) < 0.002:
        incang = 0.0
        angle=0
        px,py=0,0

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Pendulum smashing a ball (fixed)")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()
main()

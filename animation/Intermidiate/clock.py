from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin, pi
from datetime import datetime

# Window size
width, height = 500, 500
center_x, center_y = width // 2, height // 2
radius = 200  # main clock radius

def init():
    glClearColor(0, 0, 0, 1)
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # coordinate range (0,0) to (500,500)
    glMatrixMode(GL_MODELVIEW)

def draw_circle(xc, yc, r):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = 2 * pi * i / 360
        glVertex2f(xc + cos(angle) * r, yc + sin(angle) * r)
    glEnd()

def draw_hand(length, thickness):
    """Draws a rectangular hand centered at origin, pointing along +Y"""
    glBegin(GL_POLYGON)
    glVertex2f(-thickness / 2, 0)
    glVertex2f(thickness / 2, 0)
    glVertex2f(thickness / 2, length)
    glVertex2f(-thickness / 2, length)
    glEnd()

def draw_clock_face():
    # Draw main circle
    glColor3f(1, 1, 1)
    draw_circle(center_x, center_y, radius)

    # Draw hour marks
    for i in range(12):
        angle = 2 * pi * i / 12
        x1 = center_x + cos(angle) * (radius - 10)
        y1 = center_y + sin(angle) * (radius - 10)
        x2 = center_x + cos(angle) * (radius)
        y2 = center_y + sin(angle) * (radius)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Draw clock face
    draw_clock_face()

    # Get current time
    now = datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour % 12

    # Angles in radians (clockwise rotation)
    sec_angle = 2 * pi * (sec / 60)
    min_angle = 2 * pi * (minute / 60 + sec / 3600)
    hour_angle = 2 * pi * ((hour + minute / 60) / 12)

    # Draw hour hand
    glPushMatrix()
    glTranslatef(center_x, center_y, 0)
    glRotatef(-hour_angle * 180 / pi, 0, 0, 1)
    glColor3f(0.8, 0.3, 0.3)
    draw_hand(100, 10)
    glPopMatrix()

    # Draw minute hand
    glPushMatrix()
    glTranslatef(center_x, center_y, 0)
    glRotatef(-min_angle * 180 / pi, 0, 0, 1)
    glColor3f(0.3, 0.8, 0.3)
    draw_hand(140, 6)
    glPopMatrix()

    # Draw second hand
    glPushMatrix()
    glTranslatef(center_x, center_y, 0)
    glRotatef(-sec_angle * 180 / pi, 0, 0, 1)
    glColor3f(0.3, 0.3, 1.0)
    draw_hand(170, 2)
    glPopMatrix()

    glutSwapBuffers()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(1000, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Real-Time Analog Clock Coordinates")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(1000, update, 0)
    glutMainLoop()

main()

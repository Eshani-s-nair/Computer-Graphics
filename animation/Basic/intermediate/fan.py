#animation of a fan
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pi, cos, si
cx, cy = 0, 0  
angle = 0          
num_blades = 3
blade_length = 60
blade_width = 20
rotation_speed = 5
def init():
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)
def draw_circle(x, y, r, num_segments=50):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2*pi*i/num_segments
        glVertex2f(x + r*cos(theta), y + r*sin(theta))
    glEnd()
def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(cx, cy, 0)
    glRotatef(angle, 0, 0, 1)
    for i in range(num_blades):
        glPushMatrix()
        glRotatef(i * 360/num_blades, 0, 0, 1)  
        glColor3f(0,1,0)  
        glBegin(GL_POLYGON)
        glVertex2f(0, 0)
        glVertex2f(-blade_width/2, blade_length)
        glVertex2f(blade_width/2, blade_length)
        glEnd()
        glPopMatrix()
    glPopMatrix()
    glColor3f(1,1,0)
    draw_circle(cx, cy, 10)
    glutSwapBuffers()
def update(v):
    global angle
    angle += rotation_speed
    if angle >= 360:
        angle -= 360
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Rotating Fan")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

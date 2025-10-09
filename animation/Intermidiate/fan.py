from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi


x, y = 0,0        
r=10
blade_width=100
blade_length=400        
xmin, xmax = -500, 500
ymin, ymax = -500, 500
num_of_blades=3
dangle=5
angle=0

def init():
    glClearColor(0, 0, 0, 1)
    glColor3f(1.0,1.0,1.0)
    glPointSize(4)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(xmin, xmax, ymin, ymax)

def draw_circle(x, y, r, num_segments=50):
    glBegin(GL_POLYGON)
    for i in range(num_segments):
        theta = 2*pi*i/num_segments
        glVertex2f(x + r*cos(theta), y + r*sin(theta))
    glEnd()

def draw():
    global x,y,r,blade_width,blade_length,num_of_blades
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(x,y,0)
    glRotatef(angle,0,0,1)
    for i in range(num_of_blades):
        glPushMatrix()
        glRotatef(i*360/num_of_blades,0,0,1)
        glBegin(GL_TRIANGLES)
        glVertex2f(0,0)
        glVertex2f(-blade_width/2,blade_length)
        glVertex2f(blade_width/2,blade_length)
        glEnd()
        glPopMatrix()    
    glPopMatrix()
    draw_circle(x,y,20)
    glutSwapBuffers()

def update(v):
    global angle,dangle
    angle+=dangle
    if angle>=360:
        angle-=360
    glutPostRedisplay()
    glutTimerFunc(16,update,0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Bouncing Ball (Diagonal)")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

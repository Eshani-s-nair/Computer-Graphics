#rotating triangle wrt to a reference point
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
angle = 0 
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-200, 200, -200, 200)
def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    xr, yr = 0, 25  # Reference point    
    glPushMatrix()
    glTranslatef(xr, yr, 0)   
    glRotatef(angle, 0, 0, 1) 
    glTranslatef(-xr, -yr, 0)  
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 25)
    glVertex2f(-25, -25)
    glVertex2f(25, -25)
    glEnd()
    glPopMatrix()
    glutSwapBuffers()
    angle += 1
    if angle >= 360:
        angle = 0
def timer(v):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)   
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Rotating Polygon")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, timer, 0)
    glutMainLoop()
main()

from OpenGL.GL import *
from OpenGL.GLUT import *   
from OpenGL.GLU import *

width, height = 500, 500
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    glColor3f(1.0, 1.0, 1.0)
    glPointSize(4.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
def display():
    glClear(GL_COLOR_BUFFER_BIT)  
    glBegin(GL_POINTS)
    glVertex2i(width//2,height//2 )
    glEnd()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Hello OpenGL")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
if __name__ == "__main__":
    main()            
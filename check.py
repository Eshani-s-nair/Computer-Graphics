#flower
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

squares = [
    [0, 0, 72],
    [72, 72, 144],
    [144, 144, 288],
    [288, 288, 360]
]

x, y = 0, 0       
inc = 2           
current = 0        

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)    

def draw_square():
    glBegin(GL_LINE_LOOP)
    glVertex2f(-100, 100)
    glVertex2f(100, 100)
    glVertex2f(100, -100)
    glVertex2f(-100, -100)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(1, 0, 0)  
    glPushMatrix()
    glTranslatef(x, y, 0)
    for i in range(min(current + 1, len(squares))):
        angle = squares[i][0]
        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        draw_square()
        glPopMatrix()

    glPopMatrix()
    glutSwapBuffers()

def update(v):
    global current
    if current < len(squares):
        squares[current][0] += inc
        if squares[current][0] >= squares[current][2]:
            squares[current][0] = squares[current][2]
            current += 1
    glutPostRedisplay()
    glutTimerFunc(100, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Flower using Squares ")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

#scailing of a line wrt origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x1,y1,x2,y2=50,100,200,250
sx,sy=2,2
def init():
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    glPointSize(5.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 0, 500)
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glEnd() 
    x1_s, y1_s, x2_s, y2_s = scale(x1,y1,x2,y2)
    print("Scaled Line Coordinates: ", x1_s, y1_s, x2_s, y2_s)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2i(x1_s,y1_s)
    glVertex2i(x2_s,y2_s)
    glEnd()
    glFlush()   
def scale(x1,y1,x2,y2): 
    x1_scaled=x1*sx
    y1_scaled=y1*sy
    x2_scaled=x2*sx
    y2_scaled=y2*sy
    return int(x1_scaled),int(y1_scaled),int(x2_scaled),int(y2_scaled)  
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Line Scaling Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
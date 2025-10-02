#scaling of quadrilateral wrt origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
x1,y1,x2,y2=100,100,300,200
x3,y3,x4,y4=300,300,100,300
sx,sy=0.5,0.5
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
    glBegin(GL_QUADS)
    glVertex2i(x1,y1)
    glVertex2i(x2,y2)
    glVertex2i(x3,y3)
    glVertex2i(x4,y4)
    glEnd()
    x1_s, y1_s, x2_s, y2_s, x3_s, y3_s, x4_s, y4_s = scale(x1,y1,x2,y2,x3,y3,x4,y4)
    print("Scaled Shape Coordinates: ", x1_s, y1_s, x2_s, y2_s, x3_s, y3_s, x4_s, y4_s)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_QUADS)
    glVertex2i(x1_s,y1_s)
    glVertex2i(x2_s,y2_s)
    glVertex2i(x3_s,y3_s)
    glVertex2i(x4_s,y4_s)
    glEnd()
    glFlush()
def scale(x1,y1,x2,y2,x3,y3,x4,y4): 
    x1_scaled=x1*sx
    y1_scaled=y1*sy
    x2_scaled=x2*sx
    y2_scaled=y2*sy
    x3_scaled=x3*sx
    y3_scaled=y3*sy
    x4_scaled=x4*sx
    y4_scaled=y4*sy
    return int(x1_scaled),int(y1_scaled),int(x2_scaled),int(y2_scaled),int(x3_scaled),int(y3_scaled),int(x4_scaled),int(y4_scaled)      
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"OpenGL Quadrilateral Scaling Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()    
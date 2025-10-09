#animation of a fan
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pi, cos, sin


cx, cy = 0, 0     
planets={
    0 : [0,0,15,135,0,1,1,0],
    1 : [100,0,20,45,2,1,0,1],
    2:[200,0,10,60,3,1,0,0],
    3 :[-400,0,40,90,1,0,1,0]
} 
def init():
    glClearColor(0,0,0,1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)

def draw_circle(x, y, r):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,361,10):
        xr,yr=x+r*cos(i*pi/180),y+r*sin(i*pi/180)
        glVertex2f(xr,yr)
    glEnd()

def draw_tcircle(x, y, r):
    glBegin(GL_LINE_LOOP)
    for i in range(0,361,10):
        xr,yr=x+r*cos(i*pi/180),y+r*sin(i*pi/180)
        glVertex2f(xr,yr) 
    glEnd()    

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    for i in range(4):
        glTranslatef(cx,cy,0)
        glRotatef(planets[i][3],0,0,1)
        glTranslatef(-cx,-cy,0)
        glColor3f(planets[i][5],planets[i][6],planets[i][7])
        draw_circle(planets[i][0],planets[i][1],planets[i][2])
        glColor3f(1.0,1.0,1.0)
        draw_tcircle(0,0,planets[i][0])
    glPopMatrix()    
    glutSwapBuffers()    

def update(v):
    global planets
    for i in range(4):
        planets[i][3]+=planets[i][4]
        if planets[i][3]>=360:
            planets[i][3]-=360   
    glutPostRedisplay()
    glutTimerFunc(16,update,0)
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow(b"Rotating Fan")
    init()
    glutDisplayFunc(draw)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

main()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *


fish1_x = -11
fish2_x = 11

speed = 0.03


def draw_circle(x, y, r):

    glBegin(GL_POLYGON)

    for i in range(40):
        angle = 2 * 3.1416 * i / 40
        glVertex2f(x + r * cos(angle), y + r * sin(angle))

    glEnd()


def draw_sand():

    glColor3f(0.8, 0.7, 0.4)

    glBegin(GL_QUADS)
    glVertex2f(-10, -5)
    glVertex2f(10, -5)
    glVertex2f(10, -4)
    glVertex2f(-10, -4)
    glEnd()


def draw_seaweed():

    glColor3f(0, 0.6, 0)

    glBegin(GL_TRIANGLES)
    glVertex2f(-8, -4)
    glVertex2f(-7.5, -4)
    glVertex2f(-7.75, -2)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(-6.8, -4)
    glVertex2f(-6.3, -4)
    glVertex2f(-6.55, -2.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(6, -4)
    glVertex2f(6.5, -4)
    glVertex2f(6.25, -2)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(7.2, -4)
    glVertex2f(7.7, -4)
    glVertex2f(7.45, -2.7)
    glEnd()


def draw_stones():

    glColor3f(0.45, 0.45, 0.45)

    draw_circle(-4, -4.45, 0.35)
    draw_circle(-3.2, -4.5, 0.25)
    draw_circle(2.5, -4.45, 0.35)
    draw_circle(3.4, -4.5, 0.25)
    draw_circle(5, -4.45, 0.3)


def draw_fish_right(x, y, r, g, b):

    glColor3f(r, g, b)

    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + 1.5, y + 0.5)
    glVertex2f(x + 3, y)
    glVertex2f(x + 1.5, y - 0.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x - 0.8, y + 0.6)
    glVertex2f(x - 0.8, y - 0.6)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x + 1.2, y + 0.4)
    glVertex2f(x + 1.8, y + 0.4)
    glVertex2f(x + 1.5, y + 1.0)
    glEnd()

    glColor3f(0, 0, 0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x + 2.5, y + 0.15)
    glEnd()


def draw_fish_left(x, y, r, g, b):

    glColor3f(r, g, b)

    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x - 1.5, y + 0.5)
    glVertex2f(x - 3, y)
    glVertex2f(x - 1.5, y - 0.5)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + 0.8, y + 0.6)
    glVertex2f(x + 0.8, y - 0.6)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x - 1.2, y + 0.4)
    glVertex2f(x - 1.8, y + 0.4)
    glVertex2f(x - 1.5, y + 1.0)
    glEnd()

    glColor3f(0, 0, 0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x - 2.5, y + 0.15)
    glEnd()


def draw_aquarium():

    draw_sand()
    draw_seaweed()
    draw_stones()


def display():

    global fish1_x, fish2_x

    glClear(GL_COLOR_BUFFER_BIT)

    draw_aquarium()

    draw_fish_right(fish1_x, 1.5, 1, 0.5, 0)
    draw_fish_left(fish2_x, 0, 1, 0, 0.5)

    fish1_x += speed
    fish2_x -= speed

    if fish1_x > 11:
        fish1_x = -11

    if fish2_x < -11:
        fish2_x = 11

    glutSwapBuffers()


def timer(value):

    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)


def init():

    glClearColor(0.0, 0.5, 0.8, 1)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-10, 10, -5, 5)


glutInit()

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

glutInitWindowSize(900, 600)

glutCreateWindow(b"Basic Fish Aquarium Simulation")

init()

glutDisplayFunc(display)

glutTimerFunc(0, timer, 0)

glutMainLoop()
# Basic Fish Aquarium Simulation Using OpenGL

This is a simple beginner-level computer graphics project created using Python and PyOpenGL.  
The project shows a basic 2D aquarium scene where two fish move from opposite directions in a continuous loop.

## Project Description

The main purpose of this project is to demonstrate basic OpenGL drawing and animation concepts.  
The aquarium scene is created using simple 2D shapes such as polygons, triangles, circles, and quadrilaterals.

The project is intentionally kept simple and rudimentary so that it looks suitable for a beginner who has recently learned basic OpenGL concepts.

## Features

- Simple 2D aquarium environment
- Two fish moving from opposite directions
- Continuous looping animation
- Sand at the bottom of the aquarium
- Seaweed drawn using triangles
- Grey stones drawn using circles
- Basic shape drawing with OpenGL
- Timer-based animation using GLUT

## Technologies Used

- Python
- PyOpenGL
- OpenGL
- GLUT
- GLU

## OpenGL Concepts Used

- `glBegin()` and `glEnd()`
- `glVertex2f()`
- `glColor3f()`
- `GL_POLYGON`
- `GL_TRIANGLES`
- `GL_QUADS`
- `gluOrtho2D()`
- GLUT display function
- GLUT timer function
- Double buffering

## How to Run the Project

### 1. Install Required Libraries

Make sure Python is installed on your computer.  
Then install PyOpenGL using the following command:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### 2. Run the Program

Save the source code as:

```text
main.py
```

Then run the file using:

```bash
python main.py
```

## Project Output

After running the program, an OpenGL window will open.  
The window will show a simple aquarium scene with two fish moving from opposite directions.

When a fish moves outside the screen, it returns again from the opposite side.  
This creates a continuous looping animation.

## Controls

This project does not use any keyboard or mouse controls.  
The animation runs automatically.

## File Structure

```text
basic-fish-aquarium-simulation-opengl/
│
├── Images
├── Basic Fish Aquarium Simulation.py
└── README.md
```

## Repository Name

```text
basic-fish-aquarium-simulation-opengl
```

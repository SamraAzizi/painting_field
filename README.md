# Tkinter Painting Field

This is a simple painting application built using Python's Tkinter library. The application allows users to draw various shapes and lines in different colors on a canvas.

## Features

- Draw different shapes (line, rectangle, oval, circle, triangle) and use a pencil or eraser tool.
- Choose from a variety of colors to draw with.
- User-friendly interface with buttons for selecting shapes and colors.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How to Run

1. Ensure you have Python 3.x installed on your system.
2. Save the provided code into a file named `painting_field.py`.
3. Run the script using the command:
    ```sh
    python painting_field.py
    ```

## Usage

- **Drawing Shapes**: Click and drag the mouse on the canvas to draw the selected shape.
- **Change Color**: Click on any of the color buttons to change the drawing color.
- **Change Shape**: Click on any of the shape buttons to change the shape/tool used for drawing.

## Code Explanation

### Initialization

The script initializes a Tkinter window and a canvas for drawing:
```python
import tkinter as tk

# Set the canvas size
canvas_width = 800
canvas_height = 600

# Create a Tkinter window
window = tk.Tk()
window.title("Painting Field")

# Create a canvas widget
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

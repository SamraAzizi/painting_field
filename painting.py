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

# Variables to store the current drawing color and shape
current_color = "black"
current_shape = "line"
is_drawing = False
start_x = 0
start_y = 0
current_shape_id = None

# Function to handle mouse click events
def handle_click(event):
    global current_shape, is_drawing, start_x, start_y, current_shape_id
    is_drawing = True
    start_x = event.x
    start_y = event.y
    if current_shape == "line":
        current_shape_id = canvas.create_line(start_x, start_y, start_x, start_y, fill=current_color, width=2)
    elif current_shape == "rectangle":
        current_shape_id = canvas.create_rectangle(start_x, start_y, start_x, start_y, fill=current_color, outline="")
    elif current_shape == "oval":
        current_shape_id = canvas.create_oval(start_x, start_y, start_x, start_y, fill=current_color, outline="")
    elif current_shape == "circle":
        current_shape_id = canvas.create_oval(start_x, start_y, start_x, start_y, fill=current_color, outline="")
    elif current_shape == "triangle":
        current_shape_id = canvas.create_polygon(start_x, start_y, start_x, start_y, start_x, start_y, fill=current_color, outline="")
    elif current_shape == "pencil":
        current_shape_id = canvas.create_line(start_x, start_y, start_x, start_y, fill=current_color, width=2)
    elif current_shape == "eraser":
        current_shape_id = canvas.create_rectangle(start_x-10, start_y-10, start_x+10, start_y+10, fill="white", outline="")

# Function to handle mouse release events
def handle_release(event):
    global is_drawing, current_shape_id
    is_drawing = False
    current_shape_id = None

# Function to handle mouse movement events
def handle_motion(event):
    global is_drawing, current_shape_id
    if is_drawing and current_shape_id:
        x = event.x
        y = event.y
        if current_shape in ["line", "rectangle", "oval", "circle", "triangle", "pencil"]:
            canvas.coords(current_shape_id, start_x, start_y, x, y)

# Function to change the drawing color
def change_color(color):
    global current_color
    current_color = color

# Function to change the drawing shape
def change_shape(shape):
    global current_shape
    current_shape = shape

# List of colors
colors = ["black", "red", "blue", "green", "yellow", "cyan", "magenta", "orange", "purple", "pink", "brown", "gray", "white", "darkgreen", "darkblue"]

# Create buttons for selecting colors
color_buttons = []
for color in colors:
    button = tk.Button(window, bg=color, width=5, command=lambda c=color: change_color(c))
    color_buttons.append(button)
    button.pack(side=tk.LEFT, padx=2, pady=2)

# List of shapes
shapes = ["line", "rectangle", "oval", "circle", "triangle", "pencil", "eraser"]

# Create buttons for selecting shapes
shape_buttons = []
for shape in shapes:
    button = tk.Button(window, text=shape, width=10, command=lambda s=shape: change_shape(s))
    shape_buttons.append(button)
    button.pack(side=tk.LEFT, padx=2, pady=2)

# Bind mouse click, release, and motion events to the canvas
canvas.bind("<Button-1>", handle_click)
canvas.bind("<B1-Motion>", handle_motion)
canvas.bind("<ButtonRelease-1>", handle_release)

# Start the Tkinter event loop
window.mainloop()

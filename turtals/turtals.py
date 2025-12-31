import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Create turtle for drawing
t = turtle.Turtle()
t.speed(0)
t.color("white")
t.pensize(2)

# Functions to draw digits using turtle
def draw_digit_2(turtle, x, y, size=40, color="white"):
    """Draw the digit 2"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(0)
    # Top horizontal
    turtle.forward(size)
    # Top right vertical
    turtle.right(90)
    turtle.forward(size//2)
    # Middle horizontal
    turtle.right(90)
    turtle.forward(size)
    # Bottom left vertical
    turtle.left(90)
    turtle.forward(size//2)
    # Bottom horizontal
    turtle.left(90)
    turtle.forward(size)
    turtle.penup()

def draw_digit_0(turtle, x, y, size=40, color="white"):
    """Draw the digit 0"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(0)
    # Top horizontal
    turtle.forward(size)
    # Right vertical
    turtle.right(90)
    turtle.forward(size)
    # Bottom horizontal
    turtle.right(90)
    turtle.forward(size)
    # Left vertical
    turtle.right(90)
    turtle.forward(size)
    turtle.penup()

def draw_digit_6(turtle, x, y, size=40, color="white"):
    """Draw the digit 6"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    turtle.setheading(0)
    # Top horizontal (partial)
    turtle.forward(size//2)
    # Top right vertical down
    turtle.right(90)
    turtle.forward(size//2)
    # Middle horizontal
    turtle.right(90)
    turtle.forward(size)
    # Bottom right vertical up
    turtle.left(90)
    turtle.forward(size//2)
    # Bottom horizontal
    turtle.left(90)
    turtle.forward(size)
    # Left vertical
    turtle.left(90)
    turtle.forward(size)
    turtle.penup()

def draw_2026(turtle, start_x, start_y, size=40, colors=None):
    """Draw 2026 using turtle drawing"""
    if colors is None:
        colors = ["white"] * 4
    x = start_x
    # Draw 2
    draw_digit_2(turtle, x, start_y, size, colors[0])
    x += size + 10
    # Draw 0
    draw_digit_0(turtle, x, start_y, size, colors[1])
    x += size + 10
    # Draw 2
    draw_digit_2(turtle, x, start_y, size, colors[2])
    x += size + 10
    # Draw 6
    draw_digit_6(turtle, x, start_y, size, colors[3])

def draw_flower(turtle, x, y, size=20, color="white"):
    """Draw a flower"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    
    # Draw petals in a circle
    for i in range(6):
        turtle.setheading(i * 60)
        turtle.forward(size)
        turtle.left(30)
        turtle.circle(size//3, 60)
        turtle.left(30)
        turtle.forward(size)
        turtle.goto(x, y)
    
    # Draw center
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(size//4)
    turtle.penup()

def draw_heart(turtle, x, y, size=15, color="white"):
    """Draw a heart"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    
    # Draw heart shape
    turtle.setheading(0)
    turtle.left(140)
    turtle.forward(size)
    turtle.circle(-size//2, 200)
    turtle.setheading(60)
    turtle.forward(size)
    turtle.circle(-size//2, 200)
    turtle.forward(size)
    turtle.penup()

def draw_letter_H(turtle, x, y, size=40, color="white"):
    """Draw letter H - improved"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pensize(4)
    turtle.pendown()
    # Left vertical
    turtle.setheading(90)
    turtle.forward(size)
    # Crossbar
    turtle.backward(size//2)
    turtle.right(90)
    turtle.forward(size * 0.7)
    # Right vertical
    turtle.left(90)
    turtle.forward(size//2)
    turtle.backward(size)
    turtle.penup()

def draw_letter_A(turtle, x, y, size=40, color="white"):
    """Draw letter A - improved"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pensize(4)
    turtle.pendown()
    # Left side
    turtle.setheading(90)
    turtle.forward(size)
    # Top to right
    turtle.right(90)
    turtle.forward(size * 0.35)
    # Right side down
    turtle.right(90)
    turtle.forward(size//2)
    # Crossbar
    turtle.backward(size//2)
    turtle.left(90)
    turtle.forward(size * 0.3)
    # Complete right side
    turtle.left(90)
    turtle.forward(size//2)
    turtle.penup()

def draw_letter_P(turtle, x, y, size=40, color="white"):
    """Draw letter P - improved"""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pensize(4)
    turtle.pendown()
    # Left vertical
    turtle.setheading(90)
    turtle.forward(size)
    # Top horizontal
    turtle.right(90)
    turtle.forward(size * 0.6)
    # Top right curve
    turtle.right(90)
    turtle.forward(size * 0.4)
    # Bottom right curve
    turtle.right(90)
    turtle.forward(size * 0.6)
    # Back to middle
    turtle.backward(size * 0.6)
    turtle.left(90)
    turtle.backward(size * 0.4)
    turtle.penup()

def draw_letter_Y(turtle, x, y, size=40, color="white"):
    """Draw letter Y - improved"""
    turtle.penup()
    turtle.goto(x + size * 0.35, y)
    turtle.color(color)
    turtle.pensize(4)
    turtle.pendown()
    # Top left
    turtle.setheading(135)
    turtle.forward(size * 0.5)
    # Back to center
    turtle.backward(size * 0.5)
    # Top right
    turtle.setheading(45)
    turtle.forward(size * 0.5)
    # Down the middle
    turtle.setheading(270)
    turtle.forward(size * 0.5)
    turtle.penup()

def draw_HAPPY(turtle, start_x, start_y, size=40, color="white"):
    """Draw HAPPY horizontally - improved"""
    x = start_x
    draw_letter_H(turtle, x, start_y, size, color)
    x += size * 0.8
    draw_letter_A(turtle, x, start_y, size, color)
    x += size * 0.8
    draw_letter_P(turtle, x, start_y, size, color)
    x += size * 0.8
    draw_letter_P(turtle, x, start_y, size, color)
    x += size * 0.8
    draw_letter_Y(turtle, x, start_y, size, color)

# Step 1: Draw flowers at the start (as gifts)
t.penup()
draw_flower(t, -280, 150, 25, "white")
draw_flower(t, -260, 180, 20, "white")
draw_flower(t, -300, 180, 20, "white")
draw_flower(t, -270, 120, 18, "white")

# Draw "Happy" horizontally using turtle - improved
draw_HAPPY(t, -220, 150, 45, "white")

# Draw flowers on the right side (as gifts)
draw_flower(t, 100, 150, 25, "white")
draw_flower(t, 120, 180, 20, "white")
draw_flower(t, 80, 180, 20, "white")
draw_flower(t, 110, 120, 18, "white")

# Draw "2026" using turtle drawing in white
draw_2026(t, -100, 50, 50, ["white", "white", "white", "white"])

# Draw hearts around "2026" (as gifts)
draw_heart(t, -150, 80, 12, "white")
draw_heart(t, -150, 20, 12, "white")
draw_heart(t, 150, 80, 12, "white")
draw_heart(t, 150, 20, 12, "white")

# Draw "DevPath" at the bottom
t.goto(-80, -150)
t.color("white")
t.pendown()
t.write("DevPath", font=("Arial", 24, "normal"))
t.penup()

# Draw "=> Dev With MSayedQ" text below DevPath
t.goto(-120, -190)
t.color("white")
t.pendown()
t.write("=> Dev With MSayedQ", font=("Arial", 18, "normal"))
t.penup()

# Draw hearts at the end (as gifts)
draw_heart(t, 180, -150, 18, "white")
draw_heart(t, 210, -140, 15, "white")
draw_heart(t, 200, -170, 15, "white")
draw_heart(t, 230, -160, 12, "white")

# Hide turtle and keep window open
t.hideturtle()
turtle.done()

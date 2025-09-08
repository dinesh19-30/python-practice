import turtle

# Create a screen
screen = turtle.Screen()
screen.title("Simple Drawing with Python")

# Create a turtle
pen = turtle.Turtle()

# Draw a square
for _ in range(4):
    pen.forward(100)   # move forward
    pen.right(90)      # turn right

screen.mainloop()

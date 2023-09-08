import turtle as t
import random

timmy = t.Turtle()
# timmy.shape("turtle")
timmy.color("blue")

# Challenge 1 - Draw a square.
# for i in range(4):
#   timmy.forward(100)
#   timmy.right(90)

# Challenge 2 - Draw a dashed line.
# for i in range(15):
#   timmy.forward(10)
#   timmy.penup()
#   timmy.forward(10)
#   timmy.pendown()

# Challenge 3 - Drawing different shapes.
# colours = ["spring green", "red", "orange", "blue", "black", "hot pink", "deep sky blue", "dark gray"]
# side = 3
# while side <= 10:
#   timmy.color(random.choice(colours))
#   for i in range(side):
#     angle = 360 / side
#     timmy.forward(100)
#     timmy.right(angle)
#   side += 1

# Challenge 4 - Draw a random walk.
# colours = ["spring green", "red", "orange", "blue", "black", "hot pink", "deep sky blue", "dark gray"]
# directions = [90, 180, 270, 360]
# timmy.speed(10)
# timmy.pensize(15)

# for i in range(200):
#   timmy.color(random.choice(colours))
#   timmy.setheading(random.choice(directions))
#   timmy.forward(30)

# Tuples (immutable)
# def random_color():
#   r = random.randint(0, 255)
#   g = random.randint(0, 255)
#   b = random.randint(0, 255)
#   return (r, g, b)

# directions = [90, 180, 270, 360]
# t.colormode(255)
# timmy.speed(10)
# timmy.pensize(15)

# for i in range(200):
#   timmy.color(random_color())
#   timmy.setheading(random.choice(directions))
#   timmy.forward(30)

# Challenge 5 - Draw a spirograph.
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

t.colormode(255)
timmy.speed(15)

def draw_spirograph(size_of_gap):
  for i in range(int(360 / size_of_gap)):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
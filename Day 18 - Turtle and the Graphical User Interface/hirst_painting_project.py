import turtle as t
import random

# Part 1 - Extract the colors from the image
# import colorgram

# colors = colorgram.extract("image.jpg", 30)

# rgb_colors = []
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   rgb_colors.append((r, g, b))

# print(rgb_colors)

screen = t.Screen()
screen.setworldcoordinates(-100, -50, screen.window_width() - 50, screen.window_height() - 50)

color_list = [(199, 12, 32), (250, 237, 19), (39, 76, 189), (238, 228, 5), (38, 217, 68), (228, 159, 48), (28, 40, 157), (242, 246, 252), (215, 75, 13), (15, 154, 15), (198, 15, 11), (243, 33, 166), (68, 10, 30), (228, 18, 120), (60, 15, 8), (224, 141, 209), (11, 97, 62), (223, 161, 8), (50, 211, 230), (18, 19, 45), (10, 228, 239), (237, 156, 218), (83, 73, 213), (77, 210, 164), (81, 234, 201), (58, 233, 242), (5, 68, 42)]

timmy = t.Turtle()
timmy.up()
timmy.speed("fastest")
timmy.hideturtle()
t.colormode(255)


for row in range(10):
  for column in range(10):
    timmy.dot(20, random.choice(color_list))
    x = timmy.position()
    timmy.setx(x[0] + 50)
  
  timmy.setx(0)
  timmy.sety(timmy.position()[1] + 50)



screen.exitonclick()

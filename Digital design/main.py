import turtle as t
import colorsys
import random


t.screensize(canvwidth=400, canvheight=400)
#gradient was made with chatgpt
def convert_color(rgb):
    return tuple(c/255 for c in rgb)

def interpolate(start_color, end_color, factor: float):

    r = start_color[0] + factor * (end_color[0] - start_color[0])
    g = start_color[1] + factor * (end_color[1] - start_color[1])
    b = start_color[2] + factor * (end_color[2] - start_color[2])
    return (r, g, b)

def draw_gradient(start_color, end_color, width, height):
    t.setup(width, height)
    t.speed(0)
    t.bgcolor("white")
    t.up()
    t.goto(-width//2, height//2)
    t.down()
    t.setheading(-90)

    for i in range(height):
        color = interpolate(start_color, end_color, i / height)
        t.color(color)
        t.forward(1)
        t.left(90)
        t.forward(width)
        t.back(width)
        t.right(90)

    t.hideturtle()


colors = [(251, 10, 22), (247, 175, 60), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128)]


start_color = convert_color(random.choice(colors))  
end_color = convert_color(random.choice(colors))   

draw_gradient(start_color, end_color, 800, 1000)



t.goto(0, 0)
t.addshape("iphone2.gif")
t.shape("iphone2.gif")
t.stamp()

t.addshape("apli.gif")
t.shape("apli.gif")
t.stamp()

t.up()
t.color(end_color)
t.goto(0, 300)
t.write("Apple", align="center", font=("SF Pro", 90, "normal"))
t.up()

t.goto(0, -300)
t.color(start_color)
t.write("Mondays", align="center", font=("SF Pro", 90, "normal"))
t.goto(0, -400)
t.write("10:30 - 14:00", align="center", font=("SF Pro", 90, "normal"))




t.mainloop()



from turtle import *

#we want to paint a house#we want to paint a house

#step 1: draw a square
speed(5)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill

penup()
goto(170, 170)
pendown()
color("blue")
right(60)
forward(40)

left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)




penup()
goto(30, 170)
pendown()
color("blue")


right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)












exitonclick()
from turtle import *

#start drawing of sun

penup()
speed(30)

forward(480)
left(90)

forward(380)

pendown()
color("yellow")

begin_fill()
circle(60)
end_fill()

penup()

goto(440, 315)
pendown()

width(4)

left(180)
forward(50)

left(180)

forward(50)

penup()

left(90)

forward(70)
right(70)
forward(10)
left(70)

pendown()

left(60)
forward(50)
left(180)
forward(50)

penup()

left(50)
forward(50)
left(70)
forward(3)
pendown()

forward(50)

penup()
color("black")
goto(0, 0)
pendown()

# end of drawing sun

#start of drawing house(1)

left(180)
penup()

forward(70)
pendown()

begin_fill()
forward(160)
left(90)
forward(180)
left(90)
forward(160)
left(90)
forward(180)

left(180)
forward(180)

end_fill()

color("red")
begin_fill()
right(40)
forward(120)
right(98)
forward(126)

end_fill()

penup()
goto(120, 0)
pendown()

color("blue")
begin_fill()

left(138)
forward(100)
right(90)
forward(60)
right(90)
forward(100)

right(90)
forward(63)

end_fill()

#end of drawing house(1)


color("black")
penup()
goto(0, 0)

forward(90)
pendown()

#start of drawing house(2)

color("cyan")
begin_fill()
right(90)
forward(180)
left(90)
forward(150)
left(90)
forward(180)
left(90)
forward(150)
left(90)
forward(180)
left(40)
end_fill()

color("purple")
begin_fill()
forward(120)
left(102)
forward(120)
end_fill()

penup()
goto(-132, 1)
pendown()

color("black")
begin_fill()
right(142)
forward(100)
left(90)
forward(60)
left(90)
forward(100)
left(90)
forward(60)
end_fill()

#end of drawing house(2)

#making ground
penup()
goto(0, 0)
pendown()

color("green")
forward(500)
left(180)
forward(1000)
#end of drawing ground

penup()
goto(0, 0)
pendown()

#start of drawing tree(1)

forward(330)
color("brown")
begin_fill()
right(90)
forward(90)
left(90)
forward(40)
left(90)
forward(90)
left(90)
forward(40)
end_fill()

left(90)
forward(90)
color("green")
right(90)
begin_fill()
forward(35)
left(90)
forward(80)
left(90)
forward(110)
left(90)
forward(80)
left(90)
forward(100)
end_fill()

#end of drawing tree(1)

penup()
goto(0, 0)
forward(10)
pendown()

#start of drawing tree(2)

color("brown")
begin_fill()
left(90)
forward(90)
left(90)
forward(40)
left(90)
forward(90)
left(90)
forward(40)
end_fill()

left(90)
forward(90)
color("green")
right(90)
begin_fill()
forward(35)
left(90)
forward(80)
left(90)
forward(110)
left(90)
forward(80)
left(90)
forward(100)
end_fill()

#end of drawing tree(2)

penup()
goto(0, 0)
forward(340)
pendown()

#start of drawing tree(3)

color("brown")
begin_fill()
left(90)
forward(90)
left(90)
forward(40)
left(90)
forward(90)
left(90)
forward(40)
end_fill()

left(90)
forward(90)
color("green")
right(90)
begin_fill()
forward(35)
left(90)
forward(80)
left(90)
forward(110)
left(90)
forward(80)
left(90)
forward(100)
end_fill()


#end of drawing tree(3)

penup()
goto(174, 50)
pendown()

color("black")
circle(5)

color("red")
penup()
goto (-140, 45)
pendown()
circle(5)

penup()
goto(0, 0)
pendown()



















exitonclick()

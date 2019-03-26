import turtle
z=turtle.Screen()
h=turtle.Turtle()
h.speed(2)
for i in range(100):
     h.circle(5*i)
     h.circle(-5*i)
     h.left(i)
turtle.exitonclick()
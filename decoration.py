import turtle
h = turtle.Turtle()
h.speed(10)
cl = ["red", "green", "blue"]

def art(d,angle,x,y):
     c = 0
     h.up()
     h.goto(x,y)
     h.down()
     for i in range(1, 400):
          h.pencolor(cl[c])
          h.forward(d)
          h.left(angle)
          d = d - 1
          c = c + 1
          if c > 2:
               c = 0
art(150,98,0,0)






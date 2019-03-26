import turtle
h = turtle.Screen()
h.bgcolor("light green")
h.title("Turtle")
m=turtle.Turtle()
m.color("blue")
def sqr(size):
     for i in range(4):
          m.fd(size)
          m.left(90)
          size=size-5
sqr(146)
sqr(126)
sqr(106)
sqr(86)
sqr(66)
sqr(46)
sqr(26)
sqr(16)






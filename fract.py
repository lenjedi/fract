import turtle
import math
def fract(leng):
  turtle.seth(225)
  turtle.forward(leng)
  if leng>3:
    fract(leng/2)
  turtle.seth(225)
  turtle.backward(leng)
  turtle.left(90)
  turtle.forward(leng)
  if leng>3:
    fract(leng/2)
  turtle.seth(315)
  turtle.backward(leng)
def Main():
  leng=float(input("how big? "))
  y=math.sqrt(2*(leng**2))
  y=y/2
  turtle.penup()
  turtle.sety(y)
  turtle.down()
  turtle.color("black")
  fract(leng)
  turtle.done
if __name__ == "__main__":
  Main()

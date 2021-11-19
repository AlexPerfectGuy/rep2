import turtle
from random import randint
a = list(map(int, input().split()))

for i in range(0, len(a)-1):
    turtle.circle(a[i])
    turtle.up()
    turtle.setpos(randint(0, 100), randint(0, 100))
    turtle.down()

turtle.speed(0)
turtle.exitonclick()


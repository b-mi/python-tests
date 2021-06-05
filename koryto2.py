import turtle
import random

turtle.tracer(10, 0)
t = turtle.Turtle()
for uhol in range(20000):
    t.fd(8 + random.randint(-3, 3))
#    t.rt(uhol+random.randint(0, 10)/ 100)
    t.rt(uhol)

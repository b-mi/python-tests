import turtle
import random
import time

turtle.delay(0)
t = turtle.Turtle()
t.speed(10)
while True:
    uhol = random.randint(30, 170)
    for i in range(3, 600, 1):
        t.fd(i)
        t.rt(uhol)
    input("enter")
    t.reset()
    t.speed(10)

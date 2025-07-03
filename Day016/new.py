from turtle import Turtle, Screen
import time

obj = Turtle()
obj.shape("turtle")
obj.speed(60)  # Slowest allowed speed

for steps in range(30):
    for c in ('blue', 'red', 'green'):
        obj.color(c)           # use obj.color
        obj.forward(steps)     # use obj.forward
        obj.right(30)          # use obj.right
        time.sleep(0.05) 
position = obj.pos()
print(position)
scr = Screen()
scr.mainloop()

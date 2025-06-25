from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.goto(x=random.randint(-300,300),y=random.randint(-300,300))
        #self.refresh()
    def refresh(self):
        self.goto(x=random.randint(-300,300),y=random.randint(-300,300))


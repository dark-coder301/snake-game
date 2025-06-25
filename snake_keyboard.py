from turtle import Turtle,Screen
from snake_class import Snake
class Keyboard:
    
    def __init__(self,s,segments,snake):
        self.segments=segments
        self.s=s
        self.snake=snake
        self.s.onkey(self.up,"Up")
        self.s.onkey(self.down,"Down")
        self.s.onkey(self.left,"Left")
        self.s.onkey(self.right,"Right")
    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
            self.snake.move_snake()
    def down(self):
         if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)
            self.snake.move_snake()
    def left(self):
         if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)
            self.snake.move_snake()
    def right(self):
         if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
            self.snake.move_snake()
        
    

        

from turtle import Turtle,Screen
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_FORWARD=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.borders()
    def borders(self):
         s=Screen()
         t=Turtle()
         s.tracer(0)
         t.color("white")
         t.speed("fastest")
         t.penup()
         t.goto(320,320)
         t.pendown()
         for _ in range(4):
              t.right(90)
              t.forward(640)
         s.update()
         t.hideturtle()

    def add_segment(self,position):
            s1=Turtle("square")
            s1.color("white")
            s1.speed("fast")
            s1.penup()
            s1.goto(position)
            self.segments.append(s1)
    def create_snake(self):
        for position in STARTING_POSITIONS:
             self.add_segment(position)
    def extend(self):
         self.add_segment(self.segments[-1].position())
            
    
      

    def move_snake(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(x=new_x,y=new_y)
        self.segments[0].forward(MOVE_FORWARD)
        

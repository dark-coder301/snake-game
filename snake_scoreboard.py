from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()  # Hide the turtle cursor
        self.goto(x=0, y=320)
        self.write(f"Score: {self.score}", align="center", font=("arial", 25, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()  # Clear the previous score
        self.write(f"Score: {self.score}", align="center", font=("arial", 25, "bold"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("arial", 25, "bold"))

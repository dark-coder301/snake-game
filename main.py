from turtle import Screen, Turtle
from snake_class import Snake
from snake_food import Food
from snake_keyboard import Keyboard
from snake_scoreboard import Score
import time

# Screen setup
s = Screen()
s.setup(height=750, width=750)
s.bgcolor("Black")
s.title("My Snake Game")
s.tracer(0)

# Initialize objects
snake = Snake()
food = Food()
score = Score()
s.listen()
k = Keyboard(s, snake.segments, snake)

# Read high score from file
#try:
try:
    with open("C:/Users/Tatva/Documents/python/highscores.txt", "r") as fil1:
        highscore = int(fil1.read())
except (FileNotFoundError, ValueError):
    highscore = 0  # Default to 0 if the file is missing or invalid

# except (FileNotFoundError, ValueError):
#     highscore = 0  # Default to 0 if file is missing or invalid

# Display high score
t = Turtle()
t.penup()
t.color("white")
t.hideturtle()
t.goto(0, 290)
t.write(f"Highscore: {highscore}", align="center", font=("arial", 25, "bold"))

# Game loop
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.segments[0].xcor() > 320 or snake.segments[0].xcor() < -320 or snake.segments[0].ycor() > 320 or snake.segments[0].ycor() < -320:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

# Update high score if needed
if score.score > highscore:
    with open("C:/Users/Tatva/Documents/python/highscores.txt", "w") as file:
        file.write(str(score.score))  # Write new high score as a string

s.exitonclick()

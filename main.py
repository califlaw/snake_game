from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initializing the screen and it's features
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Califlaw's Snake Game")
screen.tracer(0)

# Creating objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Here we are using buttons to control the moving of the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Check's if game is on then screen starts to update and snake uses move method that we created in snake.py Snake class

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect  collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect  collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    # Detect collision with tail.
    # if head collides with any segmnt in the tail: trigger game_over

screen.exitonclick()

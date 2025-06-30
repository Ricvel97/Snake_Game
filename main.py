from turtle import Screen
import time

from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Left", fun=snake.move_left)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

#   Detect collision with food.
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.add_point()
        snake.extension()
        snake.change_color()
        snake.change_shape()

#   Detect collision with wall.
    snake_xcor = snake.head.xcor()
    snake_ycor = snake.head.ycor()

    if snake_xcor > 295 or snake_xcor < -295:
        scoreboard.reset()
        snake.reset_snake()

    elif snake_ycor > 295 or snake_ycor < -295:
        scoreboard.reset()
        snake.reset_snake()

    #   Detect collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.move()

    def move(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        random_location = (random_xcor, random_ycor)
        self.goto(random_location)
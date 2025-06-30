from copyreg import add_extension
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for segment in STARTING_POSITION:
            self.add_segment(segment)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extension(self):
        self.add_segment(self.tail.pos())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            """range(len(segments) -1, 0, -1)
            In this code, the iteration will be done starting from last to first
            Note that [0] will not be iterated since the range() function doesn't take into account
            the second argument. Therefore, it will end in the item with index [1]"""

            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(20)

    def move_up(self):
        heading = self.head.heading()

        if heading != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        heading = self.head.heading()

        if heading != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        heading = self.head.heading()

        if heading != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        heading = self.head.heading()

        if heading != RIGHT:
            self.head.setheading(LEFT)

from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 25, "bold"))

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 25, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 25, "bold"))


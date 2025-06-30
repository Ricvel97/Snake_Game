from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(0, 260)
        self.update_score()

    def add_point(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",
                   align="center", font=("Courier", 25, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align="center", font=("Courier", 25, "bold"))


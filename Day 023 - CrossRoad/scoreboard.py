from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.write(self.score, align="center", font=FONT)

    def level_up(self):
        self.score += 1
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(self.score, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


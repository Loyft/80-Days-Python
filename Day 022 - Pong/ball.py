from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.y_move = 2
        self.x_move = 2
        self.move_speed = 0.01

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.01

    def speed_up(self):
        self.move_speed *= 0.9

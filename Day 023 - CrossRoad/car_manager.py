from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5
CHANCE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = 1
        self.new_chance = 60

    def create_car(self):
        chance = random.randint(1, self.new_chance)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            random_y = random.randint(-200, 200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
        if self.new_chance > 5:
            self.new_chance -= CHANCE_INCREMENT

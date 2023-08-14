from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.move_distance = 5
        self.cars_list = []
        self.create_car()

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 3)
        new_car.pu()
        new_car.color(choice(COLORS))
        new_car.goto((310, randint(-270, 270)))
        self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.bk(self.move_distance)

    def del_extra_car(self, car):
        self.cars_list.remove(car)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

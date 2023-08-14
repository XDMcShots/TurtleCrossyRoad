from time import sleep
from turtle import Screen
from random import randint
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

user = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(user.move, "Up")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()

    rand_choice = randint(1, 4)
    if rand_choice == 1:
        car_manager.create_car()  # only creates cars every 0.5 seconds
        for car in car_manager.cars_list:  # Delete the extra cars that are not visible on screen
            if car.xcor() < -325:
                car_manager.del_extra_car(car)
    for car in car_manager.cars_list:  # Detect collision with car - Game Over
        y_cor_dist = car.ycor()-user.ycor()
        if user.distance(car) < 40 and (21 > y_cor_dist > -20):
            scoreboard.game_over()
            game_is_on = False
    if user.ycor() > 280:  # Detect if user touches finish line
        car_manager.level_up()
        user.go_to_start()
        scoreboard.level += 1
        scoreboard.display()

    car_manager.move_cars()

screen.exitonclick()
screen.clearscreen()

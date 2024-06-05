#786
#coded by Zub1Wun
#Turtle Crossing Game from 100DaysOfCodePython Udemy course, Day 23
#Started 2024-06-04 Tues
#Completed 2024-06-05 Wed

import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MAX_X = SCREEN_WIDTH / 2
MAX_Y = SCREEN_HEIGHT / 2

# TODO : 1. A turtle moves forwards when you press the "Up" key.
#  It can only move forwards, not back, left or right.
# TODO : 2. Cars are randomly generated along the y-axis
#  and will move from the right edge of the screen to the left edge.
# TODO : 3. When the turtle hits the top edge of the screen,
#  it moves back to the original position and the player levels up.
#  On the next level, the car speed increases.
# TODO : 4. When the turtle collides with a car,
#  it's game over and everything stops.


def create_screen():
    screen = Screen()
    screen.title("Zub1Wun's Turtle Crossing Game")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    player = Player()

    car_manager = CarManager(MAX_X, MAX_Y)
    scoreboard = Scoreboard(MAX_X, MAX_Y)

    screen.listen()
    screen.onkeypress(player.move, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_cars()
        car_manager.move()

        #if player.ycor() >= player.finish_line_y:
        if player.has_reached_end():
            player.reset()
            scoreboard.level_up()
            car_manager.increase_speed()

        for car in car_manager.cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                game_is_on = False

    ###AT END OF SCREEN CODE###
    screen.exitonclick()


def main():
    # TODO : creation of screen
    create_screen()


if __name__ == '__main__':
    main()

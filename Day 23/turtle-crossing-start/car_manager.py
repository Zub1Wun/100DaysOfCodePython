from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# TODO : Create cars that are 20px high by 40px wide that are randomly
#  generated along the y-axis and move to the left edge of the screen.
#  No cars should be generated in the top and bottom 50px of the screen
#  (think of it as a safe zone for our little turtle).
#  Hint: generate a new car only every 6th time the game loop runs.
#  If you get stuck, check the video walkthrough in Step 4.




class CarManager(Turtle):

    def __init__(self, screen_side, screen_top):
        super().__init__()
        self.cars = []
        self.screen_top = screen_top
        self.screen_side = screen_side
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        top_limit = self.screen_top - 50
        bottom_limit = 0 - top_limit + 50
        side_start = self.screen_side
        chance = random.randint(1,6)

        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            #rand_y = random.randint(bottom_limit, top_limit)
            rand_y = random.randint(-9, 9) * 25
# TODO : Have a way of checking cars not overlapping each other
            new_car.goto(side_start, rand_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


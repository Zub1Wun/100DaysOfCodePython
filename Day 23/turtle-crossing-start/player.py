STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finish_line_y = self.getscreen().screensize()[1] - 20
        self.start_line_y = 0 - self.finish_line_y
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.reset()
        self.setheading(90)
        self.reset()

    def reset(self):
        self.goto(0, self.start_line_y)

    def move(self):
        self.forward(MOVE_DISTANCE)
       #y = self.ycor() + MOVE_DISTANCE
       #x = self.xcor()
       #self.goto(x, y)

    def has_reached_end(self):
        return self.ycor() >= self.finish_line_y





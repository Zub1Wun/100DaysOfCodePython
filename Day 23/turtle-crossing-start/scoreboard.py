FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Roboto", 50, "normal")

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, screen_side, screen_top):
        super().__init__()
        self.screen_side = screen_side
        self.screen_top = screen_top
        self.y_pos = screen_top - 50
        self.x_pos = 0 - screen_side
        self.color("black")
        self.level = 0
        self.penup()
        self.hideturtle()
        self.write_level()

    def write_level(self):
        self.clear()
        self.setposition(self.x_pos, self.y_pos)
        self.text = f"Level : {self.level}"
        self.write(self.text, True, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.write_level()

    def game_over(self):
        self.setposition(0, 0)
        text = "GAME OVER!"
        self.write(text, True, align="center", font=GAME_OVER_FONT)

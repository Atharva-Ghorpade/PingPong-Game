from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position, 0)

    def go_up(self):
        if self.ycor() < 245:
            new_cor = self.ycor() + 20
            self.goto(self.xcor(), new_cor)

    def go_down(self):
        if self.ycor() > -245:
            new_cor = self.ycor() - 20
            self.goto(self.xcor(), new_cor)

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.l_score = 0
        self.r_score = 0
        self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 20, 'normal'))

    def l_plus(self):
        self.l_score += 1
        self.clear()
        self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 20, 'normal'))

    def r_plus(self):
        self.r_score += 1
        self.clear()
        self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 20, 'normal'))

    def gameover(self):
        if self.l_score == 2:
            self.clear()
            self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 20, 'normal'))
            self.goto(0, 0)
            self.write(arg=f"GAME OVER!\n Left player wins!", align="center", font=('Arial', 26, 'normal'))
            return True
        elif self.r_score == 2:
            self.clear()
            self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 20, 'normal'))
            self.goto(0, 0)
            self.write(arg=f"GAME OVER!\n Right player wins!", align="center", font=('Arial', 26, 'normal'))
            return True
        else:
            return False

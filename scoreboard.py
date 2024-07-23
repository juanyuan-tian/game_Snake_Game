from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 15, 'normal'))
        self.hideturtle()

    def add_score(self):
        self.clear()
        self.score += 1
        self.goto(x=0, y=270)
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 15, 'normal'))
#         分数没有加上去

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over", True, align="center", font=('Arial', 15, 'normal'))




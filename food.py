from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # 直接在Food class里面用Turtle的功能, so self is object?
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        # get a new food
        x_coor = random.randint(-280, 280)
        y_coor = random.randint(-280, 280)
        self.goto(x_coor, y_coor)


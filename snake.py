from turtle import Turtle, Screen

# import time

# constant
STARTING_POSITON = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        #     assciated attribute within class  我的错误一是没有定义变量

        self.creat_snake()
        #     method and carry out right away  二是没有创造初始的snake，
        #     init里面method的会在object产生时候立马执行。
        self.head = self.segments[0]

    def creat_snake(self):
        for position in STARTING_POSITON:
            self.add_segment(position)

    #         上下连个函数分成两个变量，要记得pass位置变量
    def add_segment(self, position):
        square = Turtle()
        square.penup()
        square.shape("square")
        square.color("white")
        square.turtlesize(1, 1)
        # square.backward(i*20)
        square.goto(position)
        self.segments.append(square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

# screen.exitonclick()

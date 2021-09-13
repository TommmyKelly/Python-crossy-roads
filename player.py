from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.go_to_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def move_left(self):
        self.goto(self.xcor() - 10, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 10, self.ycor())

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False

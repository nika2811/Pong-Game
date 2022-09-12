from turtle import Turtle
paddle_speed = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=position[0], y=position[1])

    def go_up(self):
        new_y = self.ycor() + paddle_speed
        if new_y > 250:
            self.goto(x=self.xcor(), y=250)
        else:
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - paddle_speed
        if new_y < -250:
            self.goto(x=self.xcor(), y=-250)
        else:
            self.goto(x=self.xcor(), y=new_y)





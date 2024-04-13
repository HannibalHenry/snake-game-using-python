from turtle import Turtle
t1=Turtle()
UP=90
DOWN=270
LEFT=180
RIGHT=0
starting_position = [(0,0), (-20,0), (-40,0)]

class snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in starting_position:
           self.add_segment(position)
    def add_segment(self,position):
        t1 = Turtle("square")
        t1.color("white")
        t1.penup()
        t1.goto(position)
        self.segment.append(t1)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(20)


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
            self.head.setheading(RIGHT)
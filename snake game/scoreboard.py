from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.score}", False, "center", ("courier", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ("courier", 24, "normal"))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
from turtle import Screen
import time
from snake import snake
from food import Food
from scoreboard import Scoreboard
s=Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("snake game")
s.tracer(0)

snake=snake()
food=Food()
score=Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()
    #colisition with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #detect colistion with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        score.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over()




s.exitonclick()
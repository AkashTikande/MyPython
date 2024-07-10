import turtle

from numpy.random import random

# Create the screen
screen = turtle.Screen()
screen.title("Snake and Ball")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Create the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.speed(0)
snake.goto(0, 0)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 100)

# Create the score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(0, 250)
score_pen.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# Define the game loop
def game_loop(score=None):

    # Move the snake
    snake.forward(20)
    snake.backward(21)
    # Check if the snake has hit the ball
    if snake.distance(ball) < 15:
        # Increase the score
        score += 1
        score_pen.clear()
        score_pen.write("Score: {}".format(score), align="center", font=("Arial", 24, "normal"))

        # Move the ball to a random location
        ball.goto(random.randint(-290, 290), random.randint(-290, 290))

    # Check if the snake has hit the wall
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        # Game over
        screen.clear()
        screen.write("Game Over!", align="center", font=("Arial", 36, "normal"))
        screen.exitonclick()

    # Keep the game loop running
    screen.ontimer(game_loop, 100)

# Start the game loop
game_loop()

# Keep the screen open until the user clicks
screen.mainloop()
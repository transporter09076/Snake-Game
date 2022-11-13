#Importing required modules
import turtle
import time
import random
import sqlite3

delay = 0.1
score = 0

#Creating a window
root = turtle.Screen()
root.title("Snake game")
root.bgcolor("Blue")
root.setup(width=600, height=600)
root.tracer(0)

#Importing head of snake
head = turtle.Turtle()
head.shape("square")
head.color("White")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Creating apple in snake game
apple = turtle.Turtle()
apple.shape("circle")
apple.color("Red")
apple.speed(0)
apple.penup()
apple.goto(0,100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("0",align="center",font=("Arial",30,"normal"))

def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    

root.listen()
root.onkeypress(goup,"w")
root.onkeypress(goleft,"a")
root.onkeypress(godown,"s")
root.onkeypress(goright,"d")

segments = []

#Maingame play loop
while True:
    root.update()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        pen.clear()
        pen.write("Game Over", align="center", font=("Candara", 30, "normal"))
        break
    if head.distance(apple) < 20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        apple.goto(x,y)
        score += 1
        delay -= 0.001
        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape("square")
        newsegment.color("grey")
        newsegment.penup()
        segments.append(newsegment)
        pen.clear()
        pen.write(str(score), align="center", font=("Candara", 30, "normal"))
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            # head.goto(0, 0)
            head.direction = "stop"
            # for segment in segments:
            #     segment.goto(1000, 1000)
            # segment.clear()
            delay = 0.1    
            score = 0
            pen.clear()
            pen.write("Game Over", align="center", font=("candara", 24, "bold"))
    time.sleep(delay)


    

root.mainloop()




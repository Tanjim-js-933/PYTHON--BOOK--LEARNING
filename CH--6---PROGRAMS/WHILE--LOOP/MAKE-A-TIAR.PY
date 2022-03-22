import turtle

turtle.shape("turtle")
turtle.color("red")
turtle.begin_fill()
turtle.speed(6)

counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter = counter + 1
    
turtle.end_fill()
turtle.exitonclick()
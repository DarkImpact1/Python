import turtle
cursor = turtle.Turtle()
my_turtle_screen = turtle.Screen()
def pause():
    cursor.speed(2)
    for i in range(100):
        cursor.left(90)
def write_I_inside_heart():
    cursor.penup()
    cursor.goto(-230, 15)
    cursor.pencolor("#FFFFFF")
    cursor.write("I", font=("Helevetica", 54, "bold"))

def write_Love_inside_heart():
    cursor.penup()
    cursor.goto(-160, 15)
    cursor.pencolor("#FFFFFF")
    cursor.write("LOVE", font=("Helevetica", 54, "bold"))
def write_you_inside_heart():
    cursor.penup()
    cursor.goto(80, 15)
    cursor.pencolor("#FFFFFF")
    cursor.write("YOU", font=("Helevetica", 54, "bold"))
def draw_complete_heart():
    cursor.fillcolor("#FF0000")
    cursor.begin_fill()
    cursor.left(140)
    cursor.forward(294)
    draw_left_curve_of_heart()
    cursor.right(190)
    draw_right_curve_of_heart()
    cursor.forward(294)
    cursor.end_fill()
def draw_left_curve_of_heart():
    cursor.speed(50)
    for i in range(450):
        cursor.right(0.5)
        cursor.forward(1.2)
def draw_right_curve_of_heart():
    cursor.speed(50)
    for i in range(450):
        cursor.right(0.5)
        cursor.forward(1.2)
cursor.penup()
cursor.goto(0, -200)
cursor.pendown()
cursor.speed(50)
draw_complete_heart()
write_I_inside_heart()
write_Love_inside_heart()
write_you_inside_heart()
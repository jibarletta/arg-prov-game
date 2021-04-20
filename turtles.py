from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 0

    def write_province(self, provi, xcoord, ycoord):
        self.goto(x=xcoord, y=ycoord)
        self.write(provi, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.goto(x=250, y=0)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Courier", 30, "normal"))

    def point(self):
        self.score += 1
        self.update_score()

    def you_win(self):
        self.goto(x=250, y= -50)
        self.write("Adivinaste Todas! Felicitaciones!", align=ALIGNMENT, font=("Courier", 30, "normal"))

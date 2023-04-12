from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
<<<<<<< HEAD
        self.high_score = 0
=======
        with open("data.txt") as data:
            self.high_score = int(data.read())
>>>>>>> 74bd248 (adding files)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
<<<<<<< HEAD
=======
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
>>>>>>> 74bd248 (adding files)
        self.score = 0
        self.update_scoreboard()


from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 15, "normal")
MOVE = False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.high_score}", move=MOVE, align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     super().goto(0, 0)
    #     self.write(f"GAME OVER!", move=MOVE, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def scores(self):
        self.score += 1
        self.clear()
        self.update_score()




from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scorebaord()

    def update_scorebaord(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)
        
    def increase_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scorebaord()

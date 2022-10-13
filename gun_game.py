import random
from random import *
class shooting_game:
    def __init__(self, canvas):
        self.canvas = canvas

    def create_circle(self, x, y, r, col):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return self.canvas.create_oval(x0, y0, x1, y1, fill=col, outline="black")

    def create_target(self):
        x = random.randint(100,700)
        y = random.randint(10,50)
        shooting_game.create_circle(x, y, 20, 'red')
        shooting_game.create_circle(x, y, 15, 'white')
        shooting_game.create_circle(x, y, 8, 'red')
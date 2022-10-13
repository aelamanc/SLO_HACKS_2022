class GameOver:
    def __init__(self,canvas,score,num):
        self.canvas = canvas
        self.score = score
        self.num = num

    def make_screen(self):
        text = ""
        self.canvas.create_rectangle(0,0,1500,800,fill="white")
        self.canvas.create_text(750, 300, text="GAME OVER", fill="black", font=('Helvetica 30 bold'))
        self.canvas.create_text(750, 350, text="Score: " + str(self.score), fill="black", font=('Helvetica 20 bold'))

        if self.num == 0:
            text = "You died by gravity dash."
        elif self.num ==1:
            text = "You died by falling stars."
        elif self.num ==2:
            text = "You died by box ball."
        self.canvas.create_text(750, 500, text=text, fill="black", font=('Helvetica 12 bold'))
        self.canvas.pack()
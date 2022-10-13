from tkinter import *
from FallingStars import *
from GravityDash import *
from GameOver import *
from simple_game import *
import time

grey_pallete = ['#E8E9EB','#CCCDC6','#BBBCB6','#ACADA8','#746D69']
blue_pallete = ['#001d64','#002473','#003083','#006abc','#0098f1']
red_pallete = [' #FF0000','#BF0000', '#800000','#400000', '#000000']


def setup():
    global J
    global fallinggame
    global gGame
    global wallGame
    global Score
    fallinggame = FallingStars(c, window)
    window.bind_all("<KeyPress>", fallinggame.on_keypress)
    window.bind_all("<KeyRelease>", fallinggame.on_keyrelease)

    gGame = GravityDash(c)
    gGame.spike_move()
    window.bind("<Up>", gGame.up)
    window.bind("<Down>", gGame.down)

    wallGame = WallGame(c)
    window.bind("<Key>",wallGame.change_active_wall)

    Score = 0
    b.pack_forget()

    J = c.create_text(1325, 50, text=("Score:", Score), font=("Times New Roman", 50))

    c.pack()
    window.after(100, run)

window = Tk(className = 'Reflex Rush')
window.geometry("1500x800")
c = Canvas(window, bg = grey_pallete[2], width= 1500, height = 800)

b = Button(window, text = "Play", fg = "black", bg = "grey", command = setup, height = 10, width = 15, font = ("Times New Roman", 32))
b.pack(pady = 350)

def change():
    global Score
    global J
    Score+=1
    c.delete(J)
    J=c.create_text(1325,50, text=("Score:", Score), font=("Times New Roman", 50))

space = 0
min_space_btwn_spike = 15

space2 = 0
min_space_btwn_stars = 20

counter = 0

def run():
    #add code for what happens during different games...
    global fallinggame
    global gGame
    global wallGame
    global counter
    t=True

    if counter != 0 and counter % 30 == 0:
        change()
    global space2
    if (space2 == 0):
        fallinggame.create_stars()
        space2 += 1
    elif (space2 != min_space_btwn_stars):
        space2 += 1
    else:
        space2 = 0
    fallinggame.animate_stars()

    #what happens during Gravity Game
    gGame.spike_move()
    global space
    if (space==0):
        gGame.create_spikes()
        space+=1
    elif (space !=min_space_btwn_spike):
        space+=1
    else:
        space=0

    #for simple game
    wallGame.create_walls()

    if gGame.check_hit():
        GameOver(c,Score,0).make_screen()
        t = False
    elif fallinggame.check_hit():
        GameOver(c,Score,1).make_screen()
        t = False
    elif wallGame.ball_move():
        GameOver(c,Score,2).make_screen()
        t = False
    if t:
        window.after(50, run)
        counter += 1

window.mainloop()
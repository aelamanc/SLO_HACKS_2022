import tkinter as tk
import random
from Functions import *
import time

class FallingStars:
    def __init__(self, canvasname, window):
        self.window = window
        self.canvas = canvasname
        self.player = create_circle(canvasname, 300, 300, 10 ,"green", "black")
        self.spawn = create_wall(canvasname, 0, 0, 600, 15, "grey")
        self.bounds = 500
        self.x_vel = 0
        self.y_vel = 0
        self.direction = None
        self.starlist = []

    def move(self):
        if self.direction is not None:
            if (0 < self.canvas.coords(self.player)[0] < 600):
                self.canvas.move(self.player, self.x_vel, self.y_vel)
                self.window.after(20, self.move)
            else:
                self.boundaries()
        else:
            self.boundaries()

    def boundaries(self):
        if (self.canvas.coords(self.player)[0] >= 600):
            self.canvas.move(self.player, -5, 0)
        if (self.canvas.coords(self.player)[0] <= 0):
            self.canvas.move(self.player, 5, 0)

    def on_keypress(self, event):
        if event.keysym == "Left":
            self.direction = "left"
            self.x_vel = -5
            self.y_vel = 0
        if event.keysym == "Right":
            self.direction = "right"
            self.x_vel = 5
            self.y_vel = 0
        self.move()

    def on_keyrelease(self, event):
        self.direction = None

    def create_stars(self):
        x = random.randint(0, 582)
        points = [8.3, 0.8, 3.2, 15.2, 15.2, 5.6, 0.8, 5.6, 12.8, 15.2]
        self.starlist.append(self.canvas.create_polygon(points, outline = "black", fill = "black", width = 5))
        self.canvas.move(self.starlist[len(self.starlist)-1], x, 0)


    def animate_stars(self):
        for star in self.starlist:
            self.canvas.move(star, 0, 5)
            if self.canvas.coords(star)[1] > 400:
                self.starlist.remove(star)
                self.canvas.delete(star)

    def check_hit(self):
        if(len(self.canvas.find_overlapping(self.canvas.coords(self.player)[0],self.canvas.coords(self.player)[1],self.canvas.coords(self.player)[2],self.canvas.coords(self.player)[3])) > 1):
            return True
        else:
            return False

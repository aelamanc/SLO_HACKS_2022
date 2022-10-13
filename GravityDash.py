from Functions import *
import enum
import random

blue_pallete = ['#001d64','#002473','#003083','#006abc','#0098f1']

class Direction(enum.Enum):
    UP = 1
    DOWN = 2

buffer = 50
wall_dim = [1400, 20]
wall_offset = 25
spike_height = 20
spike_offset = 20 + wall_offset
y_loc = 550

class GravityDash:
    def __init__(self, canvas):
        self.stride = 100
        self.size = [wall_offset + buffer,y_loc,20]
        self.canvas = canvas
        self.direction = Direction.UP
        self.char = canvas.create_rectangle(self.size[0],self.size[1], self.size[0]+self.size[2], self.size[1]+self.size[2], fill=blue_pallete[3], outline = "black", width = 3)
        self.create_walls()
        self.spike_list = []
        self.spike_speed = 8
        self.bounds = self.size[0]
    def create_walls(self):
        wall_location = [self.size[0] - wall_offset,self.size[1]-wall_dim[1]]
        diff = self.stride + self.size[2] * 2
        color = blue_pallete[0]
        create_wall(self.canvas, wall_location[0],wall_location[1],wall_dim[0],wall_dim[1],color)
        create_wall(self.canvas, wall_location[0], wall_location[1]+diff, wall_dim[0], wall_dim[1],color)

    def create_spikes(self):

        diff = self.stride - spike_height

        x = random.randint(0, 3)
        if (x==0):
            self.spike_list.append(create_spike(self.canvas, self.size[0]+ wall_dim[0] - spike_offset, self.size[1]+ wall_dim[1] + diff, spike_height, blue_pallete[2], 0))
        elif (x==1):
            self.spike_list.append(create_spike(self.canvas, self.size[0]+ wall_dim[0] - spike_offset, self.size[1]+ wall_dim[1], spike_height, blue_pallete[2], 1))

    def spike_move(self):
        x = -1 * self.spike_speed
        y = 0
        for spike in self.spike_list:
            if(self.canvas.coords(spike)[0] > self.bounds):
                self.canvas.move(spike, x, y)
            else:
                self.spike_list.remove(spike)
                self.canvas.delete(spike)

    def up(self, event):
        if(self.direction!=Direction.UP):
            x = 0
            y = -1 * self.stride
            self.canvas.move(self.char, x, y)
            self.direction = Direction.UP

    def down(self, event):
        if(self.direction!=Direction.DOWN):
            x = 0
            y = self.stride
            self.canvas.move(self.char, x, y)
            self.direction = Direction.DOWN

    def check_hit(self):
        if(len(self.canvas.find_overlapping(self.canvas.coords(self.char)[0],self.canvas.coords(self.char)[1],self.canvas.coords(self.char)[2],self.canvas.coords(self.char)[3])) > 2):
            return True
        else:
            return False
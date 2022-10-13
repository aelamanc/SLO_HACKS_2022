from Functions import*
import enum
import random
buffer = 90
len = 30
width = buffer* 2 + len*2

class Wall(enum.Enum):
    LEFT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3

class WallGame:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 1000
        self.y = 300
        self.rad = 10
        self.ball_speed_x = random.choice([-2,-1,1,2])
        self.ball_speed_y = random.choice([-2,-1,1,2])
        self.active_wall = Wall.LEFT
        self.wall_list = self.create_walls()
        self.char = create_circle(self.canvas, self.x, self.y, self.rad, "Green", "Black")
        self.gameover = False

    def create_walls(self):
        buffer = 90
        len = 30
        width = buffer*2 + len*2
        wall_list = []
        wall_list.append(create_wall(self.canvas, self.x - buffer- len, self.y - buffer - len, len, width, "grey"))
        wall_list.append(create_wall(self.canvas, self.x - buffer- len, self.y - buffer - len, width, len, "grey"))
        wall_list.append(create_wall(self.canvas, self.x - buffer - len, self.y + buffer, width, len, "grey"))
        wall_list.append(create_wall(self.canvas, self.x + buffer, self.y - buffer - len, len, width, "grey"))
        return wall_list

    def ball_move(self):
        self.canvas.move(self.char, self.ball_speed_x, self.ball_speed_y)
        (lefPos, topPos, rightPos, bottomPos) = self.canvas.coords(self.char)
        # (left_wall, top_wall, right_wall, bottom_wall) = self.canvas.coords(self.active_wall)
        if lefPos - 20 <= self.x - buffer - len:
            if(self.active_wall == Wall.LEFT):
                self.ball_speed_x = -self.ball_speed_x
            else:
                for wall in self.wall_list:
                    self.canvas.delete(wall)
                self.gameover = True
                return True
        if rightPos >= self.x + buffer:
            if self.active_wall == Wall.RIGHT:
                self.ball_speed_x = -self.ball_speed_x
            else:
                for wall in self.wall_list:
                    self.canvas.delete(wall)
                self.gameover = True
                return True
        if topPos - 20 <= self.y - buffer - len:
            if self.active_wall == Wall.UP:
                self.ball_speed_y = -self.ball_speed_y
            else:
                for wall in self.wall_list:
                    self.canvas.delete(wall)
                self.gameover = True
                return True
        if bottomPos >= self.y + buffer:
            if self.active_wall == Wall.DOWN:
                self.ball_speed_y = -self.ball_speed_y
            else:
                for wall in self.wall_list:
                    self.canvas.delete(wall)
                self.gameover = True
                return True

    def change_active_wall(self, event):

        if event.char == 'd' and self.gameover == False:
            self.active_wall = Wall.RIGHT
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, len, width, "grey"))
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, width, len, "grey"))
            (create_wall(self.canvas, self.x - buffer - len, self.y + buffer, width, len, "grey"))
            (create_wall(self.canvas, self.x + buffer, self.y - buffer - len, len, width, "black"))
        elif event.char == 'w' and self.gameover == False:
            self.active_wall = Wall.UP
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, len, width, "grey"))
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, width, len, "black"))
            (create_wall(self.canvas, self.x - buffer - len, self.y + buffer, width, len, "grey"))
            (create_wall(self.canvas, self.x + buffer, self.y - buffer - len, len, width, "grey"))
        elif event.char == 's' and self.gameover == False:
            self.active_wall = Wall.DOWN
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, len, width, "grey"))
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, width, len, "grey"))
            (create_wall(self.canvas, self.x - buffer - len, self.y + buffer, width, len, "black"))
            (create_wall(self.canvas, self.x + buffer, self.y - buffer - len, len, width, "grey"))
        elif event.char == 'a' and self.gameover == False:
            self.active_wall = Wall.LEFT
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, len, width, "black"))
            (create_wall(self.canvas, self.x - buffer - len, self.y - buffer - len, width, len, "grey"))
            (create_wall(self.canvas, self.x - buffer - len, self.y + buffer, width, len, "grey"))
            (create_wall(self.canvas, self.x + buffer, self.y - buffer - len, len, width, "grey"))

def create_circle(canvas, x, y, r, fillColor, outlineColor):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill=fillColor, outline=outlineColor, width = 3)

def create_wall(canvas, x, y, l, w, color):
    x0 = x
    y0 = y
    x1 = x0 + l
    y1 = y0 + w
    return canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)

def create_spike(canvas,x,y,l,color,type):
    w=l/2
    if (type == 0):
        points = [x,y,x-w,y+l,x+w,y+l]
        return canvas.create_polygon(points,fill=color, outline=color)
    else:
        points = [x,y,x-w,y-l,x+w,y-l]
        return canvas.create_polygon(points,fill=color, outline=color)
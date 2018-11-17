
class Ball:

    def __init__(self, x=4, y=5, color=[255,0,0], sense=None):
        self.x = x
        self.y = y
        self.color = color
        self.sense = sense

    def move(self, x=0, y=0):
        self.x += x
        self.y += y
        print("x={} y={}".format(self.x,self.y))
        self.draw()
    
    def draw(self):
        self.sense.clear()
        self.sense.set_pixel(self.x, self.y, self.color[0], self.color[1], self.color[2])

        


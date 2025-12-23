import turtle as t

class Disk(object):
    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dhiehgt = height
        self.dwidth = width

    def showdisk(self):
        t.color("black")
        t.fillcolor("gray")
        t.begin_fill()
        t.forward(self.dwidth//2)
        t.left(90)
        t.forward(self.dhiehgt)
        t.left(90)
        t.forward(self.dwidth)
        t.left(90)
        t.forward(self.dhiehgt)
        t.left(90)
        t.forward(self.dwidth//2)
        t.end_fill()

    def newpos(self,xpos,ypos):
        t.penup()
        t.goto(xpos,ypos)
        t.pendown()

    def cleardisk(self):
        t.color("white")
        t.fillcolor("white")
        t.begin_fill()
        t.forward(self.dwidth//2)
        t.left(90)
        t.forward(self.dhiehgt)
        t.left(90)
        t.forward(self.dwidth)
        t.left(90)
        t.forward(self.dhiehgt)
        t.left(90)
        t.forward(self.dwidth//2)
        t.end_fill()


disk = Disk()
disk.showdisk()

class Pole(object):
    pass

class Hanoi(object):
    pass

t.mainloop()


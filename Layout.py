import turtle

class TextBox :
    def __init__(self, x: int, y: int, w: int, h: int, drawingPen: turtle.Turtle = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        if drawingPen is not None:
            self.drawingPen = drawingPen
        else:
            self.drawingPen = turtle.Turtle()
        
        self.drawingPen.hideturtle()
        self.drawingPen.speed(0)

    def drawTextBox(self, x: int = None, y: int = None, w: int = None, h: int = None):
        if x is not None :
            self.x = x
        
        if y is not None :
            self.y = y

        if y is not None :
            self.y = y
            
        if y is not None :
            self.y = y

        self.drawingPen.clear()
        self.drawingPen.penup()
        self.drawingPen.setpos(self.x, self.y)
        self.drawingPen.pendown()

        for iCount in range(2):
            self.drawingPen.forward(self.w)
            self.drawingPen.right(90)
            self.drawingPen.forward(self.h)
            self.drawingPen.right(90)
            
        self.drawingPen.penup()

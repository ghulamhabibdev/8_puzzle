from tkinter import Text
class Label:
    def __init__(self):
        self.label = Label()
    def SetText(self, text):
        self.label.config(text=text)
    def GetText(self):
        return self.label.cget("text")
    def SetPosition(self, x, y):
        self.label.place(x=x, y=y)
    def SetSize(self, width, height):
        self.label.config(width=width, height=height)
    def SetColor(self, color):
        self.label.config(fg=color)
    def SetBackgroundColor(self, color):
        self.label.config(bg=color)
    def SetFont(self, font):
        self.label.config(font=font)
    def SetBorder(self, width):
        self.label.config(bd=width)
    def SetPadding(self, padx, pady):
        self.label.config(padx=padx, pady=pady)
    def SetMargin(self, padx, pady):
        self.label.config(madx=padx, pady=pady)
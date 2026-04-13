import tkinter as tk


class Frame:
    def __init__(self):
        self.frame = None

    def SetParent(self, parent):
        self.frame = tk.Frame(parent)

    def SetHeight(self, height):
        self.frame.config(height=height)

    def SetWidth(self, width):
        self.frame.config(width=width)

    def SetSize(self, width, height):
        self.frame.config(width=width, height=height)

    def SetBackgroundColor(self, color):
        self.frame.config(bg=color)

    def SetPosition(self, x, y):
        self.frame.place(x=x, y=y)

    def GetFrame(self):
        return self.frame

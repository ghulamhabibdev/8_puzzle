from tkinter import Button
class Btn:
    def __init__(self,):
        self.button = Button()
    def SetParent(self, parent):
                self.button = Button(parent)
    def SetCommand(self, command):
                self.button.config(command=command)
    def SetText(self, text):
                self.button.config(text=text)
    def setColor(self, color):
        self.button.config(bg=color)
    def setText(self, text):
        self.button.config(text=text)
    def setHeight(self, height):
        self.button.config(height=height)
    def setWidth(self, width):
        self.button.config(width=width)
    def pack(self, **kwargs):
        self.button.pack(**kwargs)
    def grid(self, row, column, **kwargs):
        self.button.grid(row=row, column=column, **kwargs)
    def place(self, x, y):
        self.button.place(x=x, y=y)
    def disable(self):
        self.button.config(state="disabled")
    def enable(self):
        self.button.config(state="normal")
    def displayBtnDetail(self):
        print(
            f"Text: {self.button.cget('text')}, "
            f"Color: {self.button.cget('bg')}, "
            f"Height: {self.button.cget('height')}, "
            f"Width: {self.button.cget('width')}"
        )

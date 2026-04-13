from tkinter import Text


class Label:
    def __init__(self):
        self._label = Label()
    def SetText(self, text):
        self._label.config(text=text)

    def GetText(self):
        return self._label.cget("text")

    def SetPosition(self, x, y):
        self._label.place(x=x, y=y)

    def SetSize(self, width, height):
        self._label.config(width=width, height=height)

    def SetColor(self, color):
        self._label.config(fg=color)

    def SetBackgroundColor(self, color):
        self._label.config(bg=color)

    def SetFont(self, font):
        self._label.config(font=font)

    def SetBorder(self, width):
        self._label.config(bd=width)

    def SetPadding(self, padx, pady):
        self._label.config(padx=padx, pady=pady)

    def SetMargin(self, padx, pady):
        self._label.config(marginx=padx, marginy=pady)
    def GetLabel(self):
        return self._label

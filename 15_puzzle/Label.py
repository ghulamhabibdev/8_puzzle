import tkinter as tk
class Label:
    def __init__(self):
        self._label = None
    def SetParent(self, parent):
        self._label = tk.Label(parent)
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
    def GetLabel(self):
        return self._label

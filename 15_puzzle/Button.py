import tkinter as tk


class Btn:
    def __init__(self):
        self._button = None

    def SetParent(self, parent):
        self._button = tk.Button(parent)

    def SetCommand(self, command):
        self._button.config(command=command)

    def SetText(self, text):
        self._button.config(text=text)

    def setColor(self, color):
        self._button.config(bg=color)

    def setHeight(self, height):
        self._button.config(height=height)

    def setWidth(self, width):
        self._button.config(width=width)

    def pack(self, **kwargs):
        self._button.pack(**kwargs)

    def grid(self, row, column, **kwargs):
        self._button.grid(row=row, column=column, **kwargs)

    def place(self, x, y):
        self._button.place(x=x, y=y)

    def disable(self):
        self._button.config(state="disabled")

    def enable(self):
        self._button.config(state="normal")

    def GetButton(self):
        return self._button
   
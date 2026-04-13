import tkinter as tk
class Frame:
    def __init__(self):
        self.frame = None
    def SetParent(self, parent):
        self.frame = tk.Frame(parent)
    def _check(self):
        if self.frame is None:
            raise Exception("Frame not initialized. Call SetParent() first.")
    def SetHeight(self, height):
        self._check()
        self.frame.config(height=height)
    def SetWidth(self, width):
        self._check()
        self.frame.config(width=width)
    def SetSize(self, width, height):
        self._check()
        self.frame.config(width=width, height=height)
    def SetBackgroundColor(self, color):
        self._check()
        self.frame.config(bg=color)
    def SetPosition(self, x, y):
        self._check()
        self.frame.place(x=x, y=y)
    def pack(self, **kwargs):
        self._check()
        self.frame.pack(**kwargs)
    def GetFrame(self):
        self._check()
        return self.frame

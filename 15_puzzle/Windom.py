import tkinter as tk
class WindowForm:
    def __init__(self):
        self._window = tk.Tk()
        self._width = 400
        self._height = 400
        self._window.title("15 Puzzle")
        self.update_size()
    def update_size(self):
        self._window.geometry(f"{self._width}x{self._height}")
    def setHeight(self, height):
        self._height = height
        self.update_size()
    def setWidth(self, width):
        self._width = width
        self.update_size()
    def setSize(self, width, height):
        self._width = width
        self._height = height
        self.update_size()
    def centerWindow(self):
        self._window.update_idletasks()
        w = self._width
        h = self._height
        screen_w = self._window.winfo_screenwidth()
        screen_h = self._window.winfo_screenheight()
        x = (screen_w // 2) - (w // 2)
        y = (screen_h // 2) - (h // 2)
        self._window.geometry(f"{w}x{h}+{x}+{y}")
    def setBackGroundColor(self, color):
        self._window.config(bg=color)
    def setTitle(self, title):
        self._window.title(title)
    def setResizable(self, width_bool, height_bool):
        self._window.resizable(width_bool, height_bool)
    def addLabel(self, text):
        label = tk.Label(self._window, text=text)
        label.pack()
        return label
    def addButton(self, text, command):
        btn = tk.Button(self._window, text=text, command=command)
        btn.pack()
        return btn
    def addCustomButton(self, btn_obj):
        btn_obj.pack()
    def addEntry(self):
        entry = tk.Entry(self._window)
        entry.pack()
        return entry
    def clearWindow(self):
        for widget in self._window.winfo_children():
            widget.destroy()
    def displayWindowDetail(self):
        print(f"Height: {self._height}, Width: {self._width}, BG: {self._window.cget('bg')}")
    def run(self):
        self._window.mainloop()
    def GetWindowFrom(self):
        return self._window

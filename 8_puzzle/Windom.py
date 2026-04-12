import tkinter as tk
class WindowForm:
    def __init__(self):
        self.window = tk.Tk()
        self.width = 400
        self.height = 400
        self.window.title("8 Puzzle")
        self.update_size()
    def update_size(self):
        self.window.geometry(f"{self.width}x{self.height}")
    def setHeight(self, height):
        self.height = height
        self.update_size()
    def setWidth(self, width):
        self.width = width
        self.update_size()
    def setSize(self, width, height):
        self.width = width
        self.height = height
        self.update_size()
    def centerWindow(self):
        self.window.update_idletasks()
        w = self.width
        h = self.height
        screen_w = self.window.winfo_screenwidth()
        screen_h = self.window.winfo_screenheight()
        x = (screen_w // 2) - (w // 2)
        y = (screen_h // 2) - (h // 2)
        self.window.geometry(f"{w}x{h}+{x}+{y}")
    def setBackGroundColor(self, color):
        self.window.config(bg=color)
    def setTitle(self, title):
        self.window.title(title)
    def setResizable(self, width_bool, height_bool):
        self.window.resizable(width_bool, height_bool)
    def addLabel(self, text):
        label = tk.Label(self.window, text=text)
        label.pack()
        return label
    def addButton(self, text, command):
        btn = tk.Button(self.window, text=text, command=command)
        btn.pack()
        return btn
    def addEntry(self):
        entry = tk.Entry(self.window)
        entry.pack()
        return entry
    def clearWindow(self):
        for widget in self.window.winfo_children():
            widget.destroy()
    def displayWindowDetail(self):
        print(f"Height: {self.height}, Width: {self.width}, BG: {self.window.cget('bg')}")
    def run(self):
        self.window.mainloop()

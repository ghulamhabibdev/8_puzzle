import tkinter as tk
from turtle import color

import Button


class WindowForm:
    def __init__(self):
        self._window = tk.Tk()
        self._window.overrideredirect(True)
        self._width = 1200
        self._height = 800
        self._header = None
        self._body = None
        self._x = 0
        self._y = 0
        self._window.title("15 Puzzle")
        self.update_size()
        self._init_layout()
        self._build_header()

    def _init_layout(self):
        self._container = tk.Frame(self._window, bd=1, relief="solid")
        self._container.pack(fill="both", expand=True)

        self._header = tk.Frame(self._container, bg="#1e272e", height=40)
        self._header.pack(fill="x")

        self._body = tk.Frame(self._container, bg="#ecf0f1")
        self._body.pack(fill="both", expand=True)

        self._header.bind("<Button-1>", self._start_move)
        self._header.bind("<B1-Motion>", self._do_move)

    def _build_header(self, title="15 Puzzle Game"):
        self.clear_header()
        tk.Label(
            self._header,
            text=title,
            bg="#1e272e",
            fg="white",
            font=("Arial", 12, "bold"),
        ).pack(side="left", padx=10)
        control = tk.Frame(self._header, bg="#1e272e")
        control.pack(side="right")

        tk.Button(
            control, text="—", bg="#1e272e", fg="white", bd=0, command=self._minimize
        ).pack(side="left", padx=5)

        tk.Button(
            control, text="□", bg="#1e272e", fg="white", bd=0, command=self._maximize
        ).pack(side="left", padx=5)

        tk.Button(
            control,
            text="✕",
            bg="#e74c3c",
            fg="white",
            bd=0,
            command=self._window.destroy,
        ).pack(side="left", padx=5)

    def clear_header(self):
        for w in self._header.winfo_children():
            w.destroy()

    # ---------------- WINDOW CONTROLS ----------------
    def _minimize(self):
        self._window.iconify()

    def _maximize(self):
        self._window.state("zoomed")

    # ---------------- DRAG ----------------
    def _start_move(self, event):
        self._x = event.x
        self._y = event.y

    def _do_move(self, event):
        x = event.x_root - self._x
        y = event.x_root - self._y
        self._window.geometry(f"+{x}+{y}")

    # ---------------- SIZE ----------------
    def update_size(self):
        self._window.geometry(f"{self._width}x{self._height}")

    def setSize(self, w, h):
        self._width = w
        self._height = h
        self.update_size()

    # ---------------- BODY API ----------------
    def GetBody(self):
        return self._body

    def addCustomButton(self, btn_obj):
        btn_obj.pack(pady=5)

    def run(self):
        self._window.mainloop()

    def GetWindowFrom(self):
        return self._window

    def AddFrame(self, frame):
        frame.pack(fill="both", expand=True)

    def setBackgroundColor(self, color):
        self._body.configure(bg=color)

import tkinter as tk


class WindowForm:
    def __init__(self):
        self._window = tk.Tk()
        self._width = 400
        self._height = 400

        self._header = None  # ✅ store header reference
        self._body = None  # ✅ main content area

        self._window.title("15 Puzzle")
        self.update_size()

        self._init_layout()  # ✅ initialize layout

    # ---------------- Layout Setup ----------------
    def _init_layout(self):
        # Header Frame (top)
        self._header = tk.Frame(self._window, bg="#2c3e50", height=60)
        self._header.pack(fill="x")

        # Body Frame (rest of UI)
        self._body = tk.Frame(self._window, bg="#ecf0f1")
        self._body.pack(fill="both", expand=True)

    # ---------------- Header ----------------
    def createHeader(self, title="15 Puzzle Game", subtitle=None):
        # Clear previous header content
        for widget in self._header.winfo_children():
            widget.destroy()

        # Title
        title_label = tk.Label(
            self._header,
            text=title,
            bg="#2c3e50",
            fg="white",
            font=("Arial", 18, "bold"),
        )
        title_label.pack(side="left", padx=15)

        # Optional subtitle
        if subtitle:
            sub_label = tk.Label(
                self._header,
                text=subtitle,
                bg="#2c3e50",
                fg="#bdc3c7",
                font=("Arial", 10),
            )
            sub_label.pack(side="left", padx=10)

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
        self._body.config(bg=color)  

    def setTitle(self, title):
        self._window.title(title)

    def setResizable(self, width_bool, height_bool):
        self._window.resizable(width_bool, height_bool)

    def addLabel(self, text):
        label = tk.Label(self._body, text=text)
        label.pack(pady=5)
        return label

    def addButton(self, text, command):
        btn = tk.Button(self._body, text=text, command=command)
        btn.pack(pady=5)
        return btn
    def addCustomButton(self, btn_obj):
        btn_obj.pack(pady=5)
    def addEntry(self):
        entry = tk.Entry(self._body)
        entry.pack(pady=5)
        return entry
    def clearWindow(self):
        for widget in self._body.winfo_children():
            widget.destroy()

    def displayWindowDetail(self):
        print(f"Height: {self._height}, Width: {self._width}")

    def run(self):
        self._window.mainloop()

    def GetWindowFrom(self):
        return self._window

    def GetBody(self):
        return self._body  # ✅ important for custom components

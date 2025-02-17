import tkinter as tk

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Financial Planner/Tracker")
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("360x640")
        self.root.resizable(False, False)

        main_frame=tk.Frame(self.root, name="main_frame", highlightcolor="black", highlightbackground="black", highlightthickness=1) 
        main_frame.pack_propagate(False)
        main_frame.configure(height=560, width=360)
        main_frame.pack(side="top")
        self.nav_bar()

    def nav_bar(self):
        self.nav_frame = tk.Frame(self.root, height=80, borderwidth=5, border=5, width=360, highlightcolor="red", highlightbackground="red", highlightthickness=1)
        self.nav_frame.place(x=0,y=560)
        
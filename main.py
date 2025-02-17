import tkinter as tk
import backend, frontend

if __name__ == "__main__":
    root = tk.Tk()
    
    frontend.GUI(root)
    root.mainloop()
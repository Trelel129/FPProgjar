import tkinter as tk
from tkinter import ttk
import time


class CountdownWindow(tk.Toplevel):
    def __init__(self, master, countdown_value):
        super().__init__(master)
        self.configure(bg="white")
        self.overrideredirect(True)
        self.attributes('-fullscreen', True)

        self.countdown_label = ttk.Label(self, text="", font=("Arial", 120), foreground="blue", background="white")
        self.countdown_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.countdown(countdown_value)

    def countdown(self, remaining):
        if remaining <= 0:
            self.countdown_label.config("Game Start")
            time.sleep(3)
            self.destroy()
        else:
            self.countdown_label.config(text=str(remaining))
            self.after(1000, self.countdown, remaining - 1)

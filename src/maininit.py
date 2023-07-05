import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import platform
import sys


class maininit(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager
        root.load_image()
        root.create_canvas()
        root.create_widgets()

    def load_image(root):
        root.background_image = Image.open('aset/bg.png')
        root.play_btn_image = Image.open('aset/play.png')
        root.quit_btn_image = Image.open('aset/quit.png')

        if platform.system() == "Windows":
            import ctypes
            user32 = ctypes.windll.user32
            root.screen_width = user32.GetSystemMetrics(0)
            root.screen_height = user32.GetSystemMetrics(1)
        else:
            root.screen_width = 1400
            root.screen_height = 882

        root.background_image = root.background_image.resize(
            (root.screen_width, root.screen_height), Image.ANTIALIAS)
        root.play_btn_image = root.play_btn_image.resize((int(root.screen_width / 5), int(root.screen_height / 10)), Image.ANTIALIAS)
        root.quit_btn_image = root.quit_btn_image.resize((int(root.screen_width / 5), int(root.screen_height / 10)), Image.ANTIALIAS)

        root.background_photo = ImageTk.PhotoImage(root.background_image)
        root.play_btn_photo = ImageTk.PhotoImage(root.play_btn_image)
        root.quit_btn_photo = ImageTk.PhotoImage(root.quit_btn_image)

    def create_canvas(root):
        root.background_canvas = tk.Canvas(
            root, width=root.screen_width, height=root.screen_height)
        root.background_canvas.pack()
        root.background_canvas.create_image(0, 0, anchor=tk.NW, image=root.background_photo)

    def create_widgets(root):
        create_button = ttk.Button(
            root.background_canvas, image=root.play_btn_photo, command=root.show_play_menu)
        create_button.place(x=int(root.screen_width / 2.6), y=int(root.screen_height / 2))

        join_button = ttk.Button(root.background_canvas, image=root.quit_btn_photo, command=root.show_quit_menu)
        join_button.place(x=int(root.screen_width / 2.6), y=int(root.screen_height / 1.5))

    def show_play_menu(root):
        root.menu_manager.show_menu("play")

    def show_about_menu(root):
        root.menu_manager.show_menu("join")

    def show_quit_menu(root):
        sys.exit()

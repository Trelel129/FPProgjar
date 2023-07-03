import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import platform

class menu(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager
        root.load_image()
        root.create_canvas()
        root.create_widgets()

    def load_image(root):
        root.background_image = Image.open('aset/bg.png')
        # root.team_image = Image.open('aset/By Kelompok 1.png')
        # root.title_image = Image.open('aset/Title.png')
        root.create_room_btn_image = Image.open('aset/create room.png')
        root.join_room_btn_image = Image.open('aset/join room.png')

        # Get screen resolution
        if platform.system() == "Windows":
            import ctypes
            user32 = ctypes.windll.user32
            root.screen_width = user32.GetSystemMetrics(0)
            root.screen_height = user32.GetSystemMetrics(1)
        else:
            root.screen_width = 1400
            root.screen_height = 882

        # Resize images based on screen resolution
        root.background_image = root.background_image.resize((root.screen_width, root.screen_height), Image.ANTIALIAS)
        # root.team_image = root.team_image.resize((int(root.screen_width / 6), int(root.screen_height / 9)), Image.ANTIALIAS)
        # root.title_image = root.title_image.resize((int(root.screen_width / 2), int(root.screen_height / 3)), Image.ANTIALIAS)
        root.create_room_btn_image = root.create_room_btn_image.resize((int(root.screen_width / 5), int(root.screen_height / 10)), Image.ANTIALIAS)
        root.join_room_btn_image = root.join_room_btn_image.resize((int(root.screen_width / 5), int(root.screen_height / 10)), Image.ANTIALIAS)

        # Convert images to Tkinter PhotoImage objects
        root.background_photo = ImageTk.PhotoImage(root.background_image)
        # root.team_photo = ImageTk.PhotoImage(root.team_image)
        # root.title_photo = ImageTk.PhotoImage(root.title_image)
        root.create_room_btn_photo = ImageTk.PhotoImage(root.create_room_btn_image)
        root.join_room_btn_photo = ImageTk.PhotoImage(root.join_room_btn_image)

    def create_canvas(root):
        root.background_canvas = tk.Canvas(root, width=root.screen_width, height=root.screen_height)
        root.background_canvas.pack()
        root.background_canvas.create_image(0, 0, anchor=tk.NW, image=root.background_photo)
        # root.background_canvas.create_image(int(root.screen_width / 100), int(root.screen_height / 100), anchor=tk.NW, image=root.team_photo)
        # root.background_canvas.create_image(int(root.screen_width * 0.55) - int(root.screen_width / 8), int(root.screen_height / 12), anchor=tk.NW, image=root.title_photo)


    def create_widgets(root):
        create_button = ttk.Button(root.background_canvas, image=root.create_room_btn_photo, command=root.show_create_menu)
        create_button.place(x=int(root.screen_width / 2.6), y=int(root.screen_height / 2))

        join_button = ttk.Button(root.background_canvas, image=root.join_room_btn_photo, command=root.show_join_menu)
        join_button.place(x=int(root.screen_width / 2.6), y=int(root.screen_height / 1.5))

    def show_create_menu(root):
        root.menu_manager.show_menu("create")

    def show_join_menu(root):
        root.menu_manager.show_menu("join")

    # def show_how_to_play_menu(root):
    #     root.menu_manager.show_menu("how_to_play")

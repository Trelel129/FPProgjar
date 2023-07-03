import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class room(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager
        root.load_image()
        # root.create_canvas()
        root.create_widgets()

    def load_image(root):
        root.background_photo = tk.PhotoImage(file='aset/Game Room Background.png')

    def create_canvas(root):
        root.background_canvas = tk.Canvas(root, width=1920, height=1080)
        root.background_canvas.pack()
        root.background_canvas.create_image(0, 0, anchor=tk.NW, image=root.background_photo)

    def create_widgets(root):
        back_button = ttk.Button(root, text="Back to Menu", command=root.menu_manager.show_main_menu)
        back_button.pack()

        # create_button = ttk.Button(root.background_canvas, image=root.create_room_btn_photo, command=root.show_create_menu)
        # create_button.place(x=1100, y=450)

        # join_button = ttk.Button(root.background_canvas, image=root.join_room_btn_photo, command=root.show_join_menu)
        # join_button.place(x=1100, y=600)

    # def show_create_menu(root):
    #     root.menu_manager.show_menu("create")

    # def show_join_menu(root):
    #     root.menu_manager.show_menu("join")

    # def show_how_to_play_menu(root):
    #     root.menu_manager.show_menu("how_to_play")
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import platform

from countdown import CountdownWindow

class hompimpa(tk.Frame):
    def __init__(root, master, menu_manager):
        super().__init__(master)
        root.menu_manager = menu_manager
        root.pilihan = tk.StringVar()
        root.load_image()
        root.create_canvas()
        root.create_widgets()
        root.countdown_window = None
    
    def load_image(root):
        root.background_image = Image.open('aset/bg game.png')
        root.hitam_image = Image.open('aset/hitam.jpg')
        root.putih_image = Image.open('aset/putih.jpg')
        root.pilih_image = Image.open('aset/pilih.png')
        root.up_btn_image = Image.open('aset/up.png')
        root.down_btn_image = Image.open('aset/Down.png')

        if platform.system() == "Windows":
            import ctypes
            user32 = ctypes.windll.user32
            root.screen_width = user32.GetSystemMetrics(0)
            root.screen_height = user32.GetSystemMetrics(1)
        else:
            root.screen_width = 1400
            root.screen_height = 882
        
        root.background_image = root.background_image.resize((root.screen_width, root.screen_height), Image.ANTIALIAS)
        root.hitam_image = root.hitam_image.resize((300, 300), Image.ANTIALIAS)
        root.putih_image = root.putih_image.resize((300, 300), Image.ANTIALIAS)
        # root.hitam_image_rot = root.hitam_image.resize((int(root.screen_width / 5), int(root.screen_height / 10)), Image.rotate(180), Image.ANTIALIAS)
        # root.putih_image_rot = root.putih_image.resize((int(root.screen_width / 5), int(root.screen_height / 10)), Image.rotate(180), Image.ANTIALIAS)
        root.pilih_image = root.pilih_image.resize(
            (int(root.screen_width / 10), int(root.screen_height / 24)), Image.ANTIALIAS)
        root.up_btn_image = root.up_btn_image.resize((int(root.screen_width / 10), int(root.screen_height / 16)), Image.ANTIALIAS)
        root.down_btn_image = root.down_btn_image.resize((int(root.screen_width / 10), int(root.screen_height / 16)), Image.ANTIALIAS)

        root.background_photo = ImageTk.PhotoImage(root.background_image)
        root.player1_hitam_image = ImageTk.PhotoImage(root.hitam_image)
        root.player1_putih_image = ImageTk.PhotoImage(root.putih_image)
        # root.player2_hitam_image = ImageTk.PhotoImage(root.hitam_image_rot)
        # root.player2_putih_image = ImageTk.PhotoImage(root.putih_image_rot)
        root.pilih_image_photo = ImageTk.PhotoImage(root.pilih_image)
        root.up_btn_photo = ImageTk.PhotoImage(root.up_btn_image)
        root.down_btn_photo = ImageTk.PhotoImage(root.down_btn_image)
    
    def create_canvas(root):
        root.background_canvas = tk.Canvas(root, width=root.screen_width, height=root.screen_height)
        root.background_canvas.pack()
        root.background_canvas.create_image(0, 0, anchor=tk.NW, image=root.background_photo)
        root.background_canvas.create_image(int(root.screen_width * 0.475), int(root.screen_height / 6), anchor=tk.NW, image=root.pilih_image_photo)
        # root.background_canvas.create_image(int(root.screen_width * 0.36), int(
        #     root.screen_height / 5), anchor=tk.NW, image=root.up_btn_photo)
        # root.background_canvas.create_image(int(root.screen_width * 0.36), int(
        #     root.screen_height / 5), anchor=tk.NW, image=root.down_btn_photo)
        
    def create_widgets(root):
        create_button = ttk.Button(root.background_canvas, image=root.up_btn_photo, command=root.switch_to_hitam)
        create_button.place(x=int(root.screen_width * 0.35), y=int(root.screen_height * 0.6))
        create_button = ttk.Button(root.background_canvas, image=root.down_btn_photo, command=root.switch_to_putih)
        create_button.place(x=int(root.screen_width * 0.55), y=int(root.screen_height * 0.6))

    def switch_to_putih(root):
        root.background_canvas.create_image(int(root.screen_width * 0.4), int(
            root.screen_height / 3.7), anchor=tk.NW, image=root.player1_putih_image)
        # root.pilihan = 'putih'
        
    def switch_to_hitam(root):
        root.background_canvas.create_image(int(root.screen_width * 0.4), int(
            root.screen_height / 3.7), anchor=tk.NW, image=root.player1_hitam_image)
        # root.pilihan = 'hitam'
    
    # def start_game(root):
    #     root.countdown_window = CountdownWindow(root.master, 3)
    #     root.countdown_window.protocol("WM_DELETE_WINDOW", root.countdown_window.destroy)  

    #     root.countdown_window.after(1000, root.send_pilihan)
    
    # def send_pilihan(root):
        # root.menu_manager.pilihan = root.pilihan


    

    

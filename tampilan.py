from tkinter import *
from PIL import Image, ImageTk

def update_countdown(count):
    countdown.config(text=str(count)) 

    if count > 0:
        root.after(1000, update_countdown, count - 1) 
    else :
        countdown.config(text="Time's Up!") 
        hitam_button.config(state="disabled")
        putih_button.config(state="disabled")

def switch_to_putih1():
    user2.config(image=putih1) 
    tulisan1.config(text="Putih") 

def switch_to_hitam1():
    user2.config(image=hitam1)
    tulisan1.config(text="Hitam") 

def switch_to_putih2():
    user2.config(image=putih2)  
    tulisan2.config(text="Putih")

def switch_to_hitam2():
    user2.config(image=hitam2) 
    tulisan2.config(text="Hitam") 

#basenya
root = Tk()
root.title("Hompimpa")
root.configure(background="#9b59b6")

putih1 = ImageTk.PhotoImage(Image.open("aset/Putih.png").resize((300, 300)).rotate(180))
hitam1 = ImageTk.PhotoImage(Image.open("aset/Hitam.png").resize((300, 300)).rotate(180))
putih2 = ImageTk.PhotoImage(Image.open("aset/Putih.png").resize((300, 300)))
hitam2 = ImageTk.PhotoImage(Image.open("aset/Hitam.png").resize((300, 300)))

user0 = Label(root, image=putih1, background="#9b59b6")
user1 = Label(root, image=hitam1, background="#9b59b6")
user2 = Label(root, image=putih2, background="#9b59b6")

tulisan0 = Label(root, text="Putih", font=100, bg="#9b59b6", fg="white" )
tulisan1 = Label(root, text="Hitam", font=100, bg="#9b59b6", fg="white" )
tulisan2 = Label(root, text="Putih", font=100, bg="#9b59b6", fg="white" )
opponent0 = Label(root, text="OPPONENT 1", font=100, bg="#9b59b6", fg="white" )
opponent1 = Label(root, text="OPPONENT 2", font=100, bg="#9b59b6", fg="white" )

countdown = Label(root, text="", font= 500, bg="#9b59b6", fg="black")

hitam_button = Button(root, text="Hitam", command=switch_to_hitam2)
putih_button = Button(root, text="Putih", command=switch_to_putih2)

opponent0.grid(row=1, column = 4)
opponent1.grid(row=1, column = 6)
user0.grid(row=2, column=4)
user1.grid(row=2, column=6)
tulisan0.grid(row=3, column=4)
tulisan1.grid(row=3, column=6)
countdown.grid(row = 4, column=5)
tulisan2.grid(row=9, column=5)
user2.grid(row=10, column=5)
hitam_button.grid(row=11, column=4)
putih_button.grid(row=11, column=6)

update_countdown(10)
root.mainloop()
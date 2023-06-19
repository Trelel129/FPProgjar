from tkinter import *
from PIL import Image, ImageTk

def update_countdown(count):
    countdown.config(text=str(count)) 

    if count > 0:
        root.after(1000, update_countdown, count - 1) 
    else :
        countdown.config(text="Time's Up!") 

def switch_to_hitam2():
    user2.config(image=hitam2)

def switch_to_putih2():
    user2.config(image=putih2)  

#basenya
root = Tk()
root.title("Hompimpa")
root.configure(background="#9b59b6")

hitam1 = ImageTk.PhotoImage(Image.open("aset/Hitam.png").resize((300, 300)).rotate(180))
putih1 = ImageTk.PhotoImage(Image.open("aset/Putih.png").resize((300, 300)).rotate(180))
hitam2 = ImageTk.PhotoImage(Image.open("aset/Putih.png").resize((300, 300)))
putih2 = ImageTk.PhotoImage(Image.open("aset/Putih.png").resize((300, 300)))

user1 = Label(root, image=hitam1, background="#9b59b6")
user2 = Label(root, image=putih2, background="#9b59b6")
user1.grid(row=1, column=5)
user2.grid(row=10, column=5)

tulisan1 = Label(root, text="Hitam", font=100, bg="#9b59b6", fg="white" )
tulisan2 = Label(root, text="Putih", font=100, bg="#9b59b6", fg="white" )
tulisan1.grid(row=2, column=5)
tulisan2.grid(row=9, column=5)

countdown = Label(root, text="", font= 500, bg="#9b59b6", fg="black")
countdown.grid(row = 3, column=5)


hitam_button = Button(root, text="Hitam", command=switch_to_hitam2)
hitam_button.grid(row=11, column=4)

putih_button = Button(root, text="Putih", command=switch_to_putih2)
putih_button.grid(row=11, column=6)



update_countdown(5)
root.mainloop()
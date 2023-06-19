from tkinter import *
from PIL import Image, ImageTk


#basenya
root = Tk()
root.title("Hompimpa")
root.configure(background="#9b59b6")

hitam = ImageTk.PhotoImage(Image.open("aset/Hitam.png").resize((300, 300)).rotate(180))
putih = ImageTk.PhotoImage(Image.open("aset/Putih.png").resize((300, 300)))

user1 = Label(root, image=hitam)
user2 = Label(root, image=putih)
user1.grid(row=1, column=5)
user2.grid(row=10, column=5)

tulisan1 = Label(root, text="Hitam", font=100, bg="#9b59b6", fg="white" )
tulisan2 = Label(root, text="Putih", font=100, bg="#9b59b6", fg="white" )
tulisan1.grid(row=2, column=5)
tulisan2.grid(row=9, column=5)

root.mainloop()
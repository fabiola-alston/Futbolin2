from tkinter import *

window = Tk()
window.title("FIFA '95")
window.geometry("800x600")
window.configure(bg="black")

game_canvas = Canvas(window, bg="#6eadff", width=500, height=400, highlightthickness=0)
game_canvas.place(relx=0.5, rely=0.4, anchor=CENTER)

game_canvas.create_rectangle(0, 300, 500, 400, fill="#57a840", outline="#57a840")

window.mainloop()
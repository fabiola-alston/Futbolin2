import time
from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import pygame

pygame.mixer.init()
music = pygame.mixer.music.load("Sounds/music.mp3")
pygame.mixer.music.play(-1)

window = Tk()
window.title("FIFA '95")
window.geometry("800x600")
window.configure(bg="black")

game_canvas = Canvas(window, bg="#6eadff", width=400, height=300, highlightthickness=0)
game_canvas.place(relx=0.5, rely=0.4, anchor=CENTER)

class Ball:
    def __init__(self, image):
        self.image = image

    def moveBall(self):
        for i in range(5):
            game_canvas.move(self.image, 0, -10)
            time.sleep(0.05)
            window.update()


goal_field_img = Image.open("Images/goal_field.png")
goal_field_img = goal_field_img.resize((400, 266), 5)
goal_field_tk = ImageTk.PhotoImage(goal_field_img)

goalie_img = Image.open("Images/goalie2.png")
goalie_tk = ImageTk.PhotoImage(goalie_img)

ball_img = Image.open("Images/soccer_ball.png")
ball_img = ball_img.resize((40, 40), 5)
ball_tk = ImageTk.PhotoImage(ball_img)


field = game_canvas.create_image((0, 35), image=goal_field_tk, anchor=NW)
goalie = game_canvas.create_image((162, 160), image=goalie_tk, anchor=NW)
ball = game_canvas.create_image((180, 250), image=ball_tk, anchor=NW)

ball = Ball(ball)

shoot_button = Button(window, text="Shoot", font=("retro gaming", 14), bg="blue", fg="white", focuscolor="blue", borderless=1, borderwidth=2, highlightthickness=3, relief="raised", command=ball.moveBall)
shoot_button.place(relx=0.5, rely=0.8, anchor=CENTER)

# play_button = Button(window, text="Play", font=font1, borderless=1, borderwidth=2, highlightthickness=3, relief="raised",
#                          bg="#ff0000", fg="white", overbackground="#ff5252", focuscolor="#ff0000", activebackground="#ff5252", padx=3, command=gameScreen)
#     play_button.place(relx=0.5, rely=0.65, anchor=CENTER)

window.mainloop()
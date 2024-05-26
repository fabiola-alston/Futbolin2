import random
import threading
import time
from tkinter import *
from tkmacosx import *
from PIL import Image, ImageTk
import pygame

# music
pygame.mixer.init()
music = pygame.mixer.music.load("Sounds/music.mp3")
pygame.mixer.music.play(-1)

# window creation
window = Tk()
window.title("FIFA '95")
window.geometry("800x600")
window.configure(bg="black")

# setting game canvas
game_canvas = Canvas(window, bg="#6eadff", width=400, height=300, highlightthickness=0)
game_canvas.place(relx=0.5, rely=0.4, anchor=CENTER)

global GOAL_NUM, SHOOT_COUNT
GOAL_NUM, SHOOT_COUNT = 0, 0


# ball class
class Ball:
    def __init__(self, image):
        self.image = image

    # function to animate ball
    def moveBall(self, direction):
        sound = pygame.mixer.Sound("Sounds/pickupCoin.wav")
        pygame.mixer.Sound.play(sound)

        shoot_button["state"] = "disabled"

        if direction == 1:
            x = -25
            y = 18
        elif direction == 2:
            x = -15
            y = 18
        elif direction == 3:
            x = -5
            y = 18
        elif direction == 4:
            x = 5
            y = 18
        elif direction == 5:
            x = 15
            y = 18
        elif direction == 6:
            x = 25
            y = 18

        for i in range(5):
            game_canvas.move(self.image, x, -y)
            time.sleep(0.05)
            window.update()
        time.sleep(1)
        for i in range(5):
            game_canvas.move(self.image, -x, y)
            time.sleep(0.05)
            window.update()
        shoot_button["state"] = "normal"

    def shootBall(self):
        global GOAL_NUM, SHOOT_COUNT
        random_block = random.randint(1,6)
        x = 50 + (50 * (random_block - 1))

        blocked_img = Image.open("Images/blocked.png")
        blocked_tk = ImageTk.PhotoImage(blocked_img)

        blocked_area = game_canvas.create_image((x, 80), anchor=NW, image=blocked_tk)

        random_goal = random.randint(1, 6)

        self.moveBall(random_goal)

        random_penalty = random.randint(0,1)
        penalty_gol_num = 0

        if SHOOT_COUNT < 7:
            if random_goal == random_block:
                pass
            else:
                GOAL_NUM += 1
                score_label['text'] = f"SCORE: {GOAL_NUM}"

            if random_penalty == 1:
                GOAL_NUM = penalty_gol_num

            SHOOT_COUNT += 1

        elif SHOOT_COUNT >= 7:
            shoot_button["state"] = "disabled"

        game_canvas.delete(blocked_area)



# goal field image load
goal_field_img = Image.open("Images/goal_field.png")
goal_field_img = goal_field_img.resize((400, 266), 5)
goal_field_tk = ImageTk.PhotoImage(goal_field_img)

# goalie image load
goalie_img = Image.open("Images/goalie2.png")
goalie_tk = ImageTk.PhotoImage(goalie_img)

# ball image load
ball_img = Image.open("Images/soccer_ball.png")
ball_img = ball_img.resize((40, 40), 5)
ball_tk = ImageTk.PhotoImage(ball_img)

# setting image objects
field = game_canvas.create_image((0, 35), image=goal_field_tk, anchor=NW)
goalie = game_canvas.create_image((162, 160), image=goalie_tk, anchor=NW)
ball = game_canvas.create_image((180, 250), image=ball_tk, anchor=NW)

# goalie animation thread
def goalieAnimation():
    while True:
        game_canvas.move(goalie, 0, 2)
        time.sleep(0.2)
        window.update()
        game_canvas.move(goalie, 0, 2)
        time.sleep(0.2)
        window.update()
        game_canvas.move(goalie, 0, -2)
        time.sleep(0.2)
        window.update()
        game_canvas.move(goalie, 0, -2)
        time.sleep(0.2)
        window.update()

idle_anim_thread = threading.Thread(target=goalieAnimation)
idle_anim_thread.start()

# ball object from class Ball
ball = Ball(ball)

# shoot button
shoot_button = Button(window, text="SHOOT", font=("retro gaming", 14), bg="blue", fg="white", focuscolor="blue", borderless=1, borderwidth=2, highlightthickness=3, relief="raised", command=ball.shootBall)
shoot_button.place(relx=0.5, rely=0.8, anchor=CENTER)

# score text (label)
score_label = Label(window, text=f"SCORE: {GOAL_NUM}", font=("retro gaming", 14), bg="black", fg="white")
score_label.place(relx=0.3, rely=0.1, anchor=CENTER)

# run window
window.mainloop()
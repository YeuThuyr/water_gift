
from tkinter import *
import random

game_width = 600
game_height = 600
back_ground = "pink"
accept_color = "green"
deny_color = "red"
button_width = 50
button_height = 75

class random_button():
    def __init__(self):
        x = random.randint(0, (game_width//button_width)-3)*button_width
        y = random.randint(0,(game_height//button_height)-1)*button_height
        
        self.coordinate = [x, y]
        
def move_button():
    global button_1, count
    count+=1
    button_1.destroy()
    move = random_button()
    if count == 0:
        button_1 = Button(window, text="Are you sure?", command=move_button, font="Consolas, 15", fg="black", bg=deny_color)
    elif count == 1:
        button_1 = Button(window, text="You don't love me? :(", command=move_button, font="Consolas, 15", fg="black", bg=deny_color)
    elif count == 2:
        button_1 = Button(window, text="I'm super sad right now :(", command=move_button, font="Consolas, 15", fg="black", bg=deny_color)
    elif count == 3:
        button_1 = Button(window, text="Click again and I hate you >:(", command=move_button, font="Consolas, 15", fg="black", bg=deny_color)
    else: button_1 = Button(window, text="Fine! Click again already!", command=wipe, font="Consolas, 15", fg="black", bg=deny_color)
    button_1.place(x=move.coordinate[0], y=move.coordinate[1])
        
    
def message_display():
    global button_2
    canvas.delete(ALL)
    button_1.destroy(), button_2.destroy()
    canvas.create_image(300, 500, image=picture_4)
    canvas.create_image(100, 500, image=picture_5)
    canvas.create_image(510, 500, image=picture_6)
    canvas.create_image(125, 150, image=picture_7)
    canvas.create_text(game_width//2, game_height//2+20, text="I Love you too!\nNguyen Ngoc Thuy\nAwwhh, I miss you so much!", font="Consolas, 15", fill="red")
    canvas.create_image(400, 120, image=picture)
    
def wipe():
    global button_2
    canvas.delete(ALL)
    button_1.destroy(), button_2.destroy()
    canvas.create_text(game_width//2, game_height//2+25, text="Ngực lép, đùi nhỏ ni nựa\n Chắc thích ăn đấm nhể", font=("Times New Roman", 18))
    canvas.create_text(game_width//2, game_height//2+165, text="Tôi cho thêm cơ hội đó hơ hơ", font=("Times New Roman", 15))
    button_2 = Button(window, text="Yes, I love you <3", command=message_display, font="Consolas, 15", fg="black", bg=accept_color)
    button_2.place(x=210, y=400)
    canvas.create_image(300, 200, image=scaled_picture_2)
    canvas.create_image(100, 100, image=picture_3)

window = Tk()

window.resizable(False, False)

window.title("8/3 Greeting!")

canvas = Canvas(window, width=game_width, height=game_height, bg=back_ground)
canvas.pack()

picture = PhotoImage(file="c:\\Users\\thien\\Pictures\\Camera Roll\\tải xuống.png")
picture_1 = PhotoImage(file="c:\\Users\\thien\\Pictures\\Camera Roll\\1f979.png")
picture_2 = PhotoImage(file="c:\\Users\\thien\\Pictures\\Camera Roll\\1f44a.png")
picture_3 = PhotoImage(file="c:\\Users\\thien\\Pictures\\Camera Roll\\tải xuống (2).png")
picture_4 = PhotoImage(file="c:\\Users\\thien\\Pictures\\Camera Roll\\tải xuống (1).png")
picture_5 = PhotoImage(file="f:\\Downloads\\ezgif.com-animated-gif-maker.gif")
picture_6 = PhotoImage(file="f:\\Downloads\\ezgif.com-animated-gif-maker (1).gif")
picture_7 = PhotoImage(file="f:\\Downloads\\ezgif.com-animated-gif-maker (2).gif")

scaled_picture_1 = picture_1.zoom(2,2)
scaled_picture_2 = picture_2.zoom(2,2)

count = 0

window.update()

canvas.create_text(300, 100, text="Darling, Do you love me like I do?\n", font=("Times New Roman", 14))
canvas.create_image(300, 200, image=scaled_picture_1)

cord_1 = 400
cord_2 = 350

button_1 = Button(window, text="No, I hate you", command=move_button, font="Consolas, 15", fg="black", bg=deny_color)
button_1.place(x=cord_1, y=cord_2)

button_2 = Button(window, text="Yes, I love you <3", command=message_display, font="Consolas, 15", fg="black", bg=accept_color)
button_2.place(x = cord_1-300, y = cord_2)

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
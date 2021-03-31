from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    global checks
    global reps
    checks = 0
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Long Break", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Short Break", fg=GREEN)
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", fg=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global checks
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        if reps % 2 == 0:
            checks = math.floor(reps / 2)
            for _ in range(checks):
                mark += "✔"
            label_checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

# Canvas
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=1, row=1)

# Timer
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_timer.grid(column=1, row=0)

# Buttons
button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

# Checkmark
label_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 24))
label_checkmark.grid(column=1, row=3)

window.mainloop()

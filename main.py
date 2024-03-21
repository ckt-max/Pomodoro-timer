from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps = 1
marks = ' '
timer = ''
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global marks
    reps = 1
    window.after_cancel(timer) # cancels an after
    marks = ' '
    canvas.itemconfig(timer_text, text='00:00')
    l1.config(text='Timer', font=('Roboto', 35, 'normal'),bg='#1D556F', fg=GREEN)

    # start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global marks

    if reps%2!=0:
        # marks = ' '
        l2.config(text=' ', fg=GREEN) # using config to change the content of the label
        l1.config(text='Work', fg = '#C2F69B')
        countdown(WORK_MIN * 60)
        reps+=1

    elif reps == 8:
        marks += '✓'
        l2.config(text=marks, fg=GREEN)
        l1.config(text='Long Break', fg='#9ADEA2')
        countdown(LONG_BREAK_MIN * 60)
        reps = 1
        marks = ' '

    elif reset == True:
        return None

    else:
        marks += '✓'
        l2.config(text=marks, fg=GREEN)
        l1.config(text='Short Break',fg=PINK)
        countdown(SHORT_BREAK_MIN * 60)
        reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(duration):
    global timer

    canvas.itemconfig(timer_text, text=time.strftime('%M:%S', time.gmtime(duration)))
    if(duration>0):
        timer = window.after(1000, countdown, duration-1)

    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
# window.minsize(500, 500)
window.config(padx=50,pady=50,bg='#1D556F')
# rem_time = countdown(5)


# Title Label
l1 = Label(text='Timer', font=('Roboto', 35, 'normal'),bg='#1D556F', fg=GREEN)
l1.grid(row=0, column=1)

# Tick
l2 = Label(text=' ', font=('Roboto', 18, 'normal'),bg='#1D556F', fg=GREEN) # foreground color gives color to text otherwise  it is not visible
l2.grid(row=2, column=1)

# Canvas widget:
canvas = Canvas(width=200, height=223, bg='#1D556F', highlightthickness=0) # set highlight thickness to 0 to remove the white border
fg=GREEN
img = PhotoImage(file='tomato.png')
canvas.create_image(200/2, 223/2, image = img)
timer_text = canvas.create_text(200/2, 135, text='00:00', fill='white', font=('Raleway', 27, 'bold'))

canvas.grid(row=1,column=1)


# countdown(5)

# Start button
start = Button(text='Start', font=('Raleway', 12, 'normal'), command=start_timer)
start.grid(row=2,column=0)

# Reset button
reset = Button(text='Reset', font=('Raleway', 12, 'normal'), command=reset_timer)
reset.grid(row=2, column=2)
window.mainloop()


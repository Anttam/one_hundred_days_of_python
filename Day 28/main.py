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
checkmark = '✓'
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  reps = 0
  marks = ''
  timer_label.config(text='Timer')
  canvas.itemconfig(timer_text, text='00:00')
  window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1
  if reps % 8 == 0:
   timer_label.config(text='Break',fg=RED)
   count_down(LONG_BREAK_MIN * 60)
  elif reps % 2 == 0:
    timer_label.config(text='Break', fg=PINK)
    count_down(SHORT_BREAK_MIN * 60)
  else:
    timer_label.config(text='Work', fg=GREEN)
    count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    
def count_down(count):
  global timer
  count_min = math.floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f'0{count_sec}'
  if count >= 0:
    timer = window.after(1000, count_down, count -1)
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
  else:
    start_timer()
    marks = ''
    for _ in range(math.floor(reps/2)):
      marks+=checkmark
    checkmarks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
    
window  = Tk()
window.title('Pomodoro Timer')
window.config(padx=100,pady=50, bg=YELLOW)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
timer_label.config(pady=20)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='Day 28/tomato.png')
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(103,130, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1,column=1)

start_button = Button(text='Start', command=start_timer, highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', command=reset_timer, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(fg=GREEN, background=YELLOW ,font=(FONT_NAME,35, 'bold'))
checkmarks_label.grid(row=3, column=1)

window.mainloop()
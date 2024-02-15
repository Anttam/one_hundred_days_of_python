from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
french_word = ''
english_word = ''
index = 0
words_left = 100

df = pd.read_csv('Day 31/data/french_words.csv')
data_dict = df.to_dict(orient='records')

def change_word():
  global english_word
  global french_word
  global index
  index = random.randint(0,words_left)
  english_word = data_dict[index]['English']
  french_word = data_dict[index]['French']
  update_word('French', french_word)


def update_word(language, new_word):
    card.itemconfig(card_title, text=language)
    card.itemconfig(card_word, text=new_word)
  
def flip_card():
    if card.itemcget(card_face, 'image') == 'front':
       card.itemconfig(card_face, image=back_img)
       update_word('English',english_word)

def reset():
   card.itemconfig(card_face, image=front_img)
   change_word()
   window.after(3000, flip_card)

def right():
  global words_left
  del data_dict[index]
  words_left -= 1
  reset()

window = Tk()
window.config(bg=BACKGROUND_COLOR ,padx=50 ,pady=50)
window.title('Flash Cards')

wrong_img = PhotoImage(file='Day 31/images/wrong.png')
right_img = PhotoImage(file='Day 31/images/right.png')
back_img = PhotoImage(file='Day 31/images/card_back.png', name='back')
front_img= PhotoImage(file='Day 31/images/card_front.png', name='front')



card = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_face = card.create_image(400, 263 ,image=front_img)
card_title = card.create_text(400, 150, text='', font=('Ariel', 40, 'italic'),fill='black')
card_word = card.create_text(400,263, text='', fill='black', font=('Ariel', 60, 'bold'), tags='word')
card.grid(column=0,row=0, columnspan=2)

change_word() 

wrong_button = Button(image=wrong_img, highlightthickness=0, border=0, command=reset)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0,border=0, command= right)
right_button.grid(row=1, column=1)

window.after(3000, flip_card)
window.mainloop()
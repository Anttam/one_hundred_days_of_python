from tkinter import *

def convert_to_km():
  miles = float(miles_entry.get())
  kilometers_label['text'] = round(miles *1.6, 2)
  
window = Tk()
window.title('miles converter')
window.config(padx=50, pady=50)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

miles_entry = Entry(width=5,bg='gray',) 
miles_entry.grid(column=1, row=0)

equals_label = Label(text=f' is equal to')
equals_label.grid(column=0, row=1)

kilometers_label = Label(text=0)
kilometers_label.grid(column=1,row=1)

km_label = Label(text=f'Km')
km_label.grid(column=2, row=1)

calculate = Button(text='Calculate', command=convert_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
from tkinter import *
from tkinter import messagebox
import string, random

def generate_password():
  password = []
  [password.append(random.choice(string.ascii_letters)) for _ in range(random.randint(8,10))]
  [password.append( random.choice(string.punctuation))  for _ in range(random.randint(2,4))]
  [password.append(random.choice(string.digits)) for _ in range(random.randint(2,4))]
  random.shuffle(password)
  password = ''.join(password)
  password_entry.insert(0,password)

def get_info():
  site = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()

  if site == '' or username =='' or password =='':
    messagebox.showerror(title='Missing Information', message='You did not enter all the information')

  else:
    is_ok = messagebox.askokcancel(title=site ,message=f'These are the details entered: \nEmail: {username} \nPassword: {password} \nIs this OK to save?')

    if is_ok:
      with open('Day 29/passwords.txt', mode='a') as password_file:
        password_file.write(f'{site} | {username} | {password}\n')
        website_entry.delete(0,END)
        password_entry.delete(0,END)




window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='Day 29/logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0 ,column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(END,'common-email@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=32, command=get_info)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
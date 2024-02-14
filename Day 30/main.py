from tkinter import *
from tkinter import messagebox
import string, random, json

def search_for_password():
  site = website_entry.get()
 
  with open('Day 30/passwords.json') as password_file:
    data = json.load(password_file)
    try:
      data[site]
    except KeyError:
      messagebox.showinfo(title='Not Found', message='That website was not found')
    else:
      messagebox.showinfo(title=site ,message=f'Email: {data[site]["Email"]}\n Password: {data[site]["Password"]}')

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
      try:

        with open('Day 30/passwords.json', mode='r') as password_file:
          data = json.load(password_file)

      except FileNotFoundError:

        with open('Day 30/passwords.json', mode='w') as password_file:
          json.dump({
            site:{
              'Email' : username,
              'Password': password
            }},password_file, indent=4)
          
      else:
          
        data.update({
          site:{
            'Email' : username,
            'Password': password
          }})
        with open('Day 30/passwords.json', mode='w') as password_file:
          json.dump(data, password_file, indent=4)

      finally:
          
          website_entry.delete(0,END)
          password_entry.delete(0,END)
    

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='Day 30/logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0 ,column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text='Search', command=search_for_password)
search_button.grid(row=1,column=2)

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
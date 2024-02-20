from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Ui:
  def __init__(self, quiz_brain:QuizBrain):
   self.quiz = quiz_brain
   self.window = Tk()
   self.window.title('Quiz Game')
   self.window.config(bg=THEME_COLOR, padx=20, pady=20)

   self.score_label = Label(bg=THEME_COLOR)
   self.score_label.grid(row=0, column=1)

   self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
   self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
   self.question_text = self.canvas.create_text(150,125, fill=THEME_COLOR, font=('Arial', 20, 'italic'), width= 280)

   self.true_image = PhotoImage(file='Day 34/images/true.png')
   self.false_image = PhotoImage(file='Day 34/images/false.png')

   self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_guess)
   self.true_button.grid(row=2, column=0)

   self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_guess)
   self.false_button.grid(row=2, column=1)

   self.get_next_question()
  
   self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg='white')
    if self.quiz.still_has_questions():
      self.score_label.config(text=f'Score: {self.quiz.score}')
      self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
    else:
      self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
      self.true_button.config(state='disabled')
      self.false_button.config(state='disabled')


  def true_guess(self):
    self.display_result(self.quiz.check_answer('true'))
  def false_guess(self):
    self.display_result(self.quiz.check_answer('false'))

  def display_result(self, answer:bool):
    if answer:
      self.canvas.config(bg='green')
    else:
      self.canvas.config(bg='red')
    self.window.after(1000, self.get_next_question)


import random
from question import Question
from data import question_data
class Quiz:
  def __init__(self):
    self.questions = []
    self.score = 0


  def check_answer(self,user_response, question):
      if user_response.lower() == question.answer.lower():
        return True
      return False
  
  def update_score(self):
     self.score+= 1
  
  def generate_questions(self, num_of_questions):
     for i in range(0, num_of_questions):
        question_to_add = question_data[random.randint(0, len(question_data)-1)]
        question = Question(question_to_add['text'], question_to_add['answer'])
        print(question.text, question.answer)
        self.questions.append(question)

  def ask_questions(self):
     print(self.questions)
     for i, question in enumerate(self.questions):
        print("\n")
        answer = input(f"Q{i+1}. {question.text} (True/False): ")
        if not self.check_answer(answer, question):
           print("That's wrong.")
           print(f"The correct answer was: {question.answer}")
           print(f"Your current score: {self.score}/{len(self.questions)}")
        else:
           self.update_score()
           print("You got it right!")
           print(f"The correct answer was {question.answer}")
           print(f"Your current score is {self.score}/{len(self.questions)}")

        
    
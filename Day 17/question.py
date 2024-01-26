class Question:
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer


  def check_answer(self,user_response):
    if user_response == self.answer:
      return True
    return False
    
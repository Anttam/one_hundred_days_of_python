import requests


res = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
res.raise_for_status()
question_data = res.json()['results']

  



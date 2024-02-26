import dotenv, os, requests
import datetime as dt

dotenv.load_dotenv()

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
SPREADSHEET_API = os.environ.get('SPREADSHEET_API')

nutritionix_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
spreadsheet_url = f'https://api.sheety.co/{SPREADSHEET_API}/workoutTracking/workouts'

nutritionix_headers = {
  'x-app-id': APP_ID,
  'x-app-key': API_KEY
}

exercise = input('Tell me what exercise you did: ')

nutritionix_req = {
  'query': exercise
}

nutritionix_res = requests.post(nutritionix_url, headers=nutritionix_headers, json=nutritionix_req)
nutritionix_res.raise_for_status()
nutritionix_data = nutritionix_res.json()

today = dt.datetime.now()

spreadsheet_req = {
  'workout':{
    'date' : today.strftime('%d/%m/%Y'),
    'time' : today.time().strftime('%X'),
    'exercise': nutritionix_data['exercises'][0]['name'],
    'duration': nutritionix_data['exercises'][0]['duration_min'],
    'calories': nutritionix_data['exercises'][0]['nf_calories']
  }
}

spreadsheet_res = requests.post(spreadsheet_url, json=spreadsheet_req)
spreadsheet_res.raise_for_status()
print(spreadsheet_res.status_code)
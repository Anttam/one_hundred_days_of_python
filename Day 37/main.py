import requests, dotenv, os, datetime as dt

dotenv.load_dotenv()

TOKEN =  os.environ.get('PIXELA_TOKEN')
USERNAME = os.environ.get('USERNAME')

def create_user():
  endpoint = 'https://pixe.la/v1/users'
  params = {
    'token':TOKEN ,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
  }
  res = requests.post(endpoint, json=params)
  print(res.text)

def create_graph(graph_id:str, graph_name:str, unit:str, int_or_float:str, color:str):
  endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs'
  headers = {
    'X-USER-TOKEN': TOKEN
  }
  params = {
    'id': graph_id,
    'name': graph_name,
    'unit': unit,
    'type': int_or_float,
    'color': color,
  }
  res = requests.post(endpoint, json=params, headers=headers)
  print(res.text)

def add_pixel(quantity:str, graph_id:str):
  endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}'
  headers = {
    'X-USER-TOKEN': TOKEN
  }
  params = {
    'date': dt.datetime.now().strftime("%Y%m%d"),
    'quantity': quantity,
  }
  res = requests.post(endpoint, json=params, headers=headers)
  print(res.text)

def update_pixel(date:str, graph_id:str, quantity:str):
  endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}/{date}'
  headers = {
    'X-USER-TOKEN': TOKEN
  }
  params = {
    'date': dt.datetime.now().strftime("%Y%m%d"),
    'quantity': quantity,
  }
  res = requests.put(endpoint, json=params, headers=headers)
  print(res.text)

def delete_pixel(graph_id:str, date:str):
  endpoint = f'https://pixe.la/v1/users/{USERNAME}/graphs/{graph_id}/{date}'
  headers = {
    'X-USER-TOKEN': TOKEN
  }
  res = requests.delete(endpoint, headers=headers)
  print(res.text)
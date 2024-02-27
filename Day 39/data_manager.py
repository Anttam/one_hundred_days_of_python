import requests, dotenv, os 
dotenv.load_dotenv()
SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_KEY = os.environ.get("SHEETY_KEY")
class DataManager:

    def __init__(self):
        self.header = {
            'authorization': f'Bearer {SHEETY_KEY}'
        }
        
    def get_data(self):
        get_url = f'https://api.sheety.co/{SHEETY_ID}/flightDeals/prices'
        res = requests.get(get_url, headers=self.header)
        res.raise_for_status()
        res_data = res.json()
        return res_data['prices']
    
    def update_data(self, new_data):
        put_url = f'https://api.sheety.co/{SHEETY_ID}/flightDeals/prices/'
        for row in new_data:
            requests.put(put_url+str(row['id']), headers=self.header, json={'price' : row})
        
            
        



       
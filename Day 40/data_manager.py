from pprint import pprint
import requests, dotenv, os
dotenv.load_dotenv()


SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_KEY = os.environ.get("SHEETY_KEY")


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers = {'authorization': f'Bearer {SHEETY_KEY}'}

    def get_destination_data(self):
        response = requests.get(url=f'https://api.sheety.co/{SHEETY_ID}/flightDeals/prices', headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{f'https://api.sheety.co/{SHEETY_ID}/flightDeals/prices'}/{city['id']}",
                headers=self.headers,
                json=new_data
            )
            print(response.text)

    def add_user(self, user):
        request = {
            'user': user
        }
        response = requests.post(f'https://api.sheety.co/{SHEETY_ID}/flightDeals/users', headers=self.headers, json=request)
        response.raise_for_status()
        print(response.text)

    def get_users(self):
        response = requests.get(f'https://api.sheety.co/{SHEETY_ID}/flightDeals/users', headers=self.headers)
        response.raise_for_status()
        return response.json()['users']


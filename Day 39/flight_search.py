from data_manager import DataManager
from flight_data import FlightData
import dotenv, os, requests

dotenv.load_dotenv()

FLIGHT_SEARCH_API = os.environ.get('FLIGHT_SEARCH_API')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.data_manger = DataManager()
        self.prices = self.data_manger.get_data()
        self.header = {
            'apikey' : FLIGHT_SEARCH_API
        }
        self.base_url = 'https://api.tequila.kiwi.com'

    def update_IATA_code(self):
        for price in self.prices:
            if price['iataCode'] == '':
                res = requests.get(self.base_url+'/locations/query',headers=self.header, params={'term': price['city']})
                res.raise_for_status()
                res_data = res.json()
                price['iataCode'] = res_data['locations'][0]['code']
        self.data_manger.update_data(self.prices)

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
        }

        res = requests.get(
            url=f"{self.base_url}/v2/search",
            headers=self.header,
            params=query,
        )
        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data





                
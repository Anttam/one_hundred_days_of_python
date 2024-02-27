from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()
flight_search = FlightSearch()
notification_manger = NotificationManager()

ORIGIN_CITY_IATA = "PHL"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.update_IATA_code(row["city"])
    data_manager.update_data(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination['lowestPrice']:
        notification_manger.sendmail('New Lower Price for flights',
                                      f'Only ${flight.price} to fly from 
                                      {flight.origin_city} to {flight.destination_city}-{flight.destination_airport},
                                        from {flight.out_date} to {flight.return_date}.')
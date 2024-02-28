from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

def get_user_info():
    user = {}
    user['firstName'] = input('What is your first name?')
    user['lastName'] = input('What is your last name?')
    email_first = input('What is your email?').lower()
    email_second = input('Type your email again.').lower()
    if email_first == email_second:
        user['email'] = email_second
    return user

ORIGIN_CITY_IATA = "PHL"

ask_add_user = input('Would you like to add a new user?').lower()
if ask_add_user == 'yes':
    get_user_info()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        users = data_manager.get_users()
        for user in users:
            notification_manager.sendmail(
                user = user,
                subject= 'Low price alert!',
                message=f"Hello {user['firstName']},\n\n Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )



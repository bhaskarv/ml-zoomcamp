import requests

url = "http://localhost:9696/predict"

customer = {
"id": 56694,
"gender": "Female",
"customer_type": "Loyal Customer",
"age": 50,
"type_of_travel": "Personal Travel",
"class": "Eco",
"flight_distance": 1133,
"seat_comfort": 5,
"departure/arrival_time_convenient": 4,
"food_and_drink": 4,
"gate_location": 4,
"inflight_wifi_service": 5,
"inflight_entertainment": 5,
"online_support": 5,
"ease_of_online_booking": 5,
"on-board_service": 1,
"leg_room_service": 5,
"baggage_handling": 4,
"checkin_service": 1,
"cleanliness": 5,
"online_boarding": 5,
"departure_delay_in_minutes": 0,
"arrival_delay_in_minutes": 0.0
}


response = requests.post(url=url, json=customer).json()

print(response)

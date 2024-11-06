import requests

customer = {"job": "student", "duration": 280, "poutcome": "failure"}
customer1 = {"job": "management", "duration": 400, "poutcome": "success"}

url = "http://localhost:9696/predict"

result = requests.post(url, json=customer1).json()
print(result)


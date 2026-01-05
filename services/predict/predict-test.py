
import requests


url = 'http://localhost:9696/predict'

customer_id = 'xyz-123'
customer = {
    "IsActiveMember":0.0,
    "Age_scaled":50.0
}


response = requests.post(url, json=customer).json()
print(response)

import requests


url = 'http://localhost:9695/predict'

customer_id = 'xyz-123'
customer = {
    "IsActiveMember":0.0,
    "Age_scaled":0.0
}


response = requests.post(url, json=customer).json()
print(response)
import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "hi"}

response = requests.post(url, json=data)
print(response.json())  # Output should be {'response': 'Hello! How can I help you?'}

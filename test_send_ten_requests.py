import requests

url = 'http://localhost:8000/'

for i in range(10):
    response = requests.post(url)
    print(response.text)
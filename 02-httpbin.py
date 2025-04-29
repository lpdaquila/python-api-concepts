import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"
data = {
    "buddy": {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
}

params = {
    "dateStart": "2023-01-01",
    "dateEnd": "2023-01-31",
}
# response = requests.get(url)
response = requests.post(url, json=data, params=params)
print(response)
# print(response.request.url)
print(response.text)
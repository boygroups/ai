import requests

api_key = "pk.a8d2a4cf04634d6a103410df83e98e5a"
location = input("Enter the location: ")

url = "https://us1.locationiq.com/v1/search"

params = {
    "key": api_key,
    "q": location,
    "format": "json"
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200 and data:
    place = data[0]

    print("\nOutput:")
    print("place_id:", place["place_id"])
    print("lat:", place["lat"])
    print("lon:", place["lon"])
    print("display_name:", place["display_name"])
else:
    print("Error:", response.status_code)

import requests

API_KEY="f897a99d971b5eef57be6fafa0d83239"

def get_location_data(location):
    if len(location) == 5 and location.isdigit():
        url = f"https://api.openweathermap.org/geo/1.0/zip?zip={location}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                location_data = data
            return {
                "lat": location_data["lat"],
                "lon": location_data["lon"],
                "name": location_data["name"],
                "state": location_data.get("state", None),
                "country": location_data["country"],
            }
        else:
            print(f"Error retrieving location data: {response.status_code}")
            return None
        
    else:
        city, state = location.split(",") if "," in location else (location, "")
        url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}{',' + state if state else ''}&limit=1&appid={API_KEY}"
        response=requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                location_data=data[0]
                return{
                    "lat": location_data["lat"],
                    "lon": location_data["lon"],
                    "name": location_data["name"],
                    "state": location_data.get("state", None),
                    "country": location_data["country"],
                }
            else:
                print(f"No location data found for {location}")
                return None
        else:
            print(f"Error: {response.status_code}")
            return None

def main():
    
    locations = []
    while True:
        enter_location=input("Enter City, State, or Zip code (or 'q' to quit or exit typing): ")
        if enter_location.lower() == "q":
            break
        locations.append(enter_location)

    for location in locations:
        data = get_location_data(location)
        if data:
            print(f"\nLocation: {data['name']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"Name: {data['name']}")
            if data.get("state"):
                print(f"State: {data['state']}")
            print(f"Country: {data['country']}")
        else:
            print(f"Location '{location}' not found")


if __name__ == "__main__":
    main()
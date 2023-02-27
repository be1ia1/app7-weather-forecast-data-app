import requests

API_KEY = '027a5072f88772ba9b3243179e525a17'

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    print(url)
    response = requests.get(url)
    data = response.json()
    nr_values = forecast_days * 8
    filtered_data = data['list'][:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data('Khmelnytskyi, UA', 1))

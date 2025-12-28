import requests

def get_weather_forecast(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        print("Success")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    data = response.json()
    #print(data.keys())
    print(data['list'][0])
    return data

def extract_forecast_data(data):
    temperatures_with_dates = []
    for forecast in data['list']:
        temperatures_with_dates.append((forecast['dt_txt'], forecast['main']['temp'], forecast['weather'][0]['description']))

    #print(temperatures_with_dates)
    return temperatures_with_dates


def group_by_day(forecast_data):
    daily_data = {} #dictionary
    for forecast in forecast_data:
        date = forecast[0].split(" ")[0] #splitting the daytime string (forecast[0])to get only date

        if date not in daily_data: #if this date isn't in dictionary of dates, adding it
            daily_data[date] = []

        daily_data[date].append(forecast[1]) #forecast[1] is the temperature

    return daily_data
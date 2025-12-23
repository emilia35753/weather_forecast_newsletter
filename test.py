from weather_data import get_weather_forecast, extract_forecast_data, group_by_day

def test_01():
    api_key = "5aad598ce580ee84bb7f06ca01883d5e"
    city = "London"
    data = get_weather_forecast(api_key, city)
    temperatures_with_dates = extract_forecast_data(data)

    for date, temp, descr in temperatures_with_dates:
        print(f"Data:{date}, temp:{temp}, description:{descr}\n")

    daily_data = group_by_day(temperatures_with_dates)
    print(daily_data)
from weather_data import get_weather_forecast, extract_forecast_data, group_by_day, get_today_forecast
from analysis import calculate_daily_stats
from visualization import create_temperature_chart, create_statistics_summary
from email_sender import send_email
import config

def test_01():
    data = get_weather_forecast(config.API_KEY, config.CITY)
    temperatures_with_dates = extract_forecast_data(data)

    #for date, temp, descr in temperatures_with_dates:
    #    print(f"Data:{date}, temp:{temp}, description:{descr}\n")

    # getting today's detailed forecast
    today_forecast = get_today_forecast(temperatures_with_dates)

    # getting 5-day forecast
    daily_data = group_by_day(temperatures_with_dates)
    #print(daily_data)
    daily_stats = calculate_daily_stats(daily_data)

    # creating charts
    create_temperature_chart(daily_stats)
    create_statistics_summary(daily_stats)

    # sending emails
    chart_files = ['temp_forecast.png', 'statistics_summary.png']

    send_email(
        sender_email=config.SENDER_EMAIL,
        sender_password=config.SENDER_PASSWORD,
        recipient_email=config.RECIPIENT_EMAIL,
        daily_stats=daily_stats,
        chart_files=chart_files,
        today_forecast=today_forecast

    )
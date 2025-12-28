import matplotlib.pyplot as plt

def create_temperature_chart(daily_stats, filename='temp_forecast.png'):
    dates = list(daily_stats.keys())
    mins = [daily_stats[date]['min'] for date in dates]
    maxs = [daily_stats[date]['max'] for date in dates]
    avgs = [daily_stats[date]['avg'] for date in dates]

    plt.figure(figsize=(10,6))

    plt.plot(dates, mins, marker='o', label='Min Temp', color='blue')
    plt.plot(dates, maxs, marker='o', label='Max Temp', color='red')
    plt.plot(dates, avgs, marker='o', label='Avg Temp', color='green')

    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('5-day Temperature Forecast')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(filename)
    print(f"Chart saved as {filename}")
    plt.close()


def create_statistics_summary(daily_stats, filename='statistics_summary.png'):
    dates = list(daily_stats.keys())
    stdevs = [daily_stats[date]['stdev'] for date in dates]

    plt.figure(figsize=(10, 6))

    plt.bar(dates, stdevs, color='orange', alpha=0.7)

    plt.xlabel('Date')
    plt.ylabel('Standard Deviation (°C)')
    plt.title('Temperature Variability by Day')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(filename)
    print(f"Chart saved as {filename}")

    plt.close()
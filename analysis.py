import statistics

def calculate_daily_stats(daily_data):
    stats = {}

    for date, temps in daily_data.items():
        if len(temps) < 2:
            continue

        stats[date] = {
            'min' : min(temps),
            'max' : max(temps),
            'avg' : sum(temps)/len(temps),
            'stdev' : statistics.stdev(temps),
        }
    #print(stats)
    return stats
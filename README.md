# Weather Forecast Newsletter
Daily weather reports with statistical analysis and visualizations. Fetches forecast data from OpenWeatherMap API, generates charts showing temperature trends and variability, and delivers reports via email.

## Features
- **5-Day Weather Forecast** - Statistical summary with min/max/avg temperatures and standard deviation
- **Today's Detailed Forecast** - 3-hour interval predictions with temperature, "feels like", and weather conditions
- **Visual Charts** - Automatically generated temperature trend graphs and variability analysis
- **Email Delivery** - HTML-formatted emails with data tables and attached charts

## Project Structure
```
weather_forecast_newsletter/
├── weather_data.py        # API calls and data extraction
├── analysis.py            # Statistical calculations
├── visualization.py       # Chart generation with Matplotlib
├── email_sender.py        # Email composition and sending
├── main.py                # Main execution script
├── config.py              # Configuration (API keys, email credentials)
├── requirements.txt       # Python dependencies
└── .gitignore             # Excludes sensitive files from version control
```

## Technologies Used
- **Python 3.12**
- **OpenWeatherMap API** - Weather data source
- **Matplotlib** - Data visualization
- **smtplib** - Email delivery
- **requests** - HTTP requests for API calls
- **statistics** - Statistical analysis


## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/emilia35753/weather_forecast_newsletter.git
cd weather-forecast-newsletter
```

### 2. Get API Key
1. Sign up at [OpenWeatherMap](https://openweathermap.org/)
2. Navigate to **API Keys** in your account
3. Copy your API key (may take 10-15 minutes to activate)


### 3. Configure Email
For **Gmail** users:
1. Enable **2-Factor Authentication** on your Google account
2. Go to **Security** → **App Passwords**
3. Generate an app password for "Mail"
4. Copy the 16-character password


### 5. Create Configuration File
Create `config.py` in the project root:
```python
# Email Configuration
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_16_char_app_password"
RECIPIENT_EMAIL = "recipient@gmail.com"

# Weather API Configuration
API_KEY = "your_openweathermap_api_key"
CITY = "London"  # Change to your city
```
**Never commit `config.py` to version control!** It's already in `.gitignore`.

## Usage

### Run Manually
```bash
python run_newsletter.py
```

This will:
1. Fetch weather data for your configured city
2. Generate temperature charts
3. Send an email with the forecast

### Example Output

The email contains:
- **Today's Detailed Forecast** - 3-hour intervals with temperature, feels like, and conditions
- **5-Day Summary Table** - Min/max/avg/standard deviation for each day
- **Two Attached Charts**:
  - Temperature trends (min/max/avg over 5 days)
  - Temperature variability (standard deviation by day)

## Author
Created by emilia35753

## Acknowledgments
Weather data provided by [OpenWeatherMap API](https://openweathermap.org/)

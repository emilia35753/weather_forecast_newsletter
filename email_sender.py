import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def create_email_body(daily_stats,  today_forecast=None):
    """
    Creates HTML email body with the statistics.

    Args:
        daily_stats: Dict with dates and their statistics
        today_forecast: List of today's 3-hour forecasts (optional)

    Returns:
        HTML string for email body
    """
    html = """
        <html>
            <body>
                <h2>Your Daily Weather Forecast</h2>
        """

    # Add today's detailed forecast if provided
    if today_forecast:
        html += """
                <h3>Today's Detailed Forecast (3-hour intervals)</h3>
                <table border="1" cellpadding="5" style="border-collapse: collapse;">
                    <tr>
                        <th>Time</th>
                        <th>Temperature (°C)</th>
                        <th>Feels Like (°C)</th>
                        <th>Conditions</th>
                    </tr>
            """

        for forecast in today_forecast:
            html += f"""
                    <tr>
                        <td>{forecast['time']}</td>
                        <td>{forecast['temp']:.1f}</td>
                        <td>{forecast['feels_like']:.1f}</td>
                        <td>{forecast['description'].capitalize()}</td>
                    </tr>
                """

        html += """
                </table>
                <br><br>
            """

    # Add 5-day summary
    html += """
                <h3>5-Day Summary</h3>
                <table border="1" cellpadding="5" style="border-collapse: collapse;">
                    <tr>
                        <th>Date</th>
                        <th>Min (°C)</th>
                        <th>Max (°C)</th>
                        <th>Avg (°C)</th>
                        <th>Variability (StDev)</th>
                    </tr>
        """

    for date, stats in daily_stats.items():
        html += f"""
                    <tr>
                        <td>{date}</td>
                        <td>{stats['min']:.1f}</td>
                        <td>{stats['max']:.1f}</td>
                        <td>{stats['avg']:.1f}</td>
                        <td>{stats['stdev']:.2f}</td>
                    </tr>
            """

    html += """
                </table>
                <br>
                <p>See the attached charts for visual analysis.</p>
            </body>
        </html>
        """

    return html


def send_email(sender_email, sender_password, recipient_email, daily_stats, chart_files, today_forecast=None):
    # sender_email: Your email address
    # sender_password: Your app password (NOT regular password)
    # recipient_email: Where to send the email
    # daily_stats: Statistics to include in email body
    # chart_files: List of chart filenames to attach

    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Your Daily Weather Forecast'

        html_body = create_email_body(daily_stats, today_forecast)
        msg.attach(MIMEText(html_body, 'html'))

        for chart_file in chart_files:
            with open(chart_file, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-Disposition', 'attachment', filename=chart_file)
                msg.attach(img)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection

        server.login(sender_email, sender_password)

        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {recipient_email}")
        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False
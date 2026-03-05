import smtplib
import schedule
import time
from email.message import EmailMessage

# --- Configuration ---
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "subscriber@example.com"

def compose_newsletter():
    """Create the email content."""
    msg = EmailMessage()
    msg['Subject'] = "Your Daily Newsletter ☕"
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    # You can integrate an API here (like NewsAPI) to get real data
    news_content = """
    <html>
        <body>
            <h1 style="color: #2e6c80;">Good Morning!</h1>
            <p>Here is your update for today:</p>
            <ul>
                <li><strong>Tech:</strong> AI continues to evolve rapidly.</li>
                <li><strong>Weather:</strong> It's looking like a clear day.</li>
                <li><strong>Quote:</strong> "The secret of getting ahead is getting started."</li>
            </ul>
            <footer style="font-size: 0.8em; color: gray;">
                You are receiving this because you subscribed to Python Automations.
            </footer>
        </body>
    </html>
    """
    msg.set_content("Please view this email in an HTML-compatible browser.")
    msg.add_alternative(news_content, subtype='html')
    return msg

def send_email():
    """Send the email via SMTP."""
    print("Attempting to send newsletter...")
    try:
        msg = compose_newsletter()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("Success! Newsletter sent.")
    except Exception as e:
        print(f"Error: {e}")

# --- Scheduling ---
# Schedule the task for 8:00 AM every day
schedule.every().day.at("08:00").do(send_email)

print("Newsletter service started. Waiting for scheduled time...")

while True:
    schedule.run_pending()
    time.sleep(60) # Check every minute

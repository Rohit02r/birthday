import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def send_email(body):

    msg = MIMEText(body)

    msg["Subject"] = "Website Interaction"
    msg["From"] = EMAIL
    msg["To"] = "rohit02r@gmail.com"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(EMAIL, APP_PASSWORD)

    server.send_message(msg)

    server.quit()
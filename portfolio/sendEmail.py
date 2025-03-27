import smtplib , ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    userEmail = "mirajulislamanik100@gmail.com"

    # I use environment variable to get password
    password = os.getenv("PASSWORD")

    receiver = "mirajulislamanik100@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host , port , context=context) as server:
        server.login(userEmail , password)
        server.sendmail(userEmail , receiver , message)
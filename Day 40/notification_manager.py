import dotenv, os, smtplib
dotenv.load_dotenv()

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
class NotificationManager:

    def sendmail( subject, message, user):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
            from_addr=email, 
            to_addrs=user['email'], 
            msg=f"Subject:{subject}\n\n{message}"
      )

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        smtp_server = 'smtp.gmail.com'
        port = 587

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", str(e))
        
if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    share_via_email = input("Do you want to share the calendar via email? (yes/no): ").lower()
    if share_via_email == 'yes':
        sender_email = os.environ.get('SENDER_EMAIL')
        sender_password = os.environ.get('SENDER_PASSWORD')
        receiver_email = os.environ.get('RECEIVER_EMAIL')
        subject = f"attendence for {[month]} {year}"
        body = f"Here's the attendence for {[month]} {year}:\n\n"

        if sender_email and sender_password and receiver_email:
            send_email(sender_email, sender_password, receiver_email, subject, body)
        else:
            print("Please set the SENDER_EMAIL, SENDER_PASSWORD, and RECEIVER_EMAIL environment variables.")
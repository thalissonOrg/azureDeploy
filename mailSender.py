import smtplib
import os
import email.message

# Get email credentials and other information from environment variables
from_email = os.environ.get('EMAIL_USERNAME')
password = os.environ.get('EMAIL_PASSWORD')
to_email = os.environ.get('TO_EMAIL')
message = os.environ.get('MESSAGE')
subject = os.environ.get('SUBJECT')


if from_email is None or to_email is None or message is None or password is None:
    print("Please set the environment variables: FROM_EMAIL, TO_EMAIL, EMAIL_MESSAGE, and EMAIL_PASSWORD")
    exit(1)

# Create an email message
msg = email.message.Message()
msg.set_payload(message)
msg['Subject'] = subject


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.rset()
server.quit()

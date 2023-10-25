import smtplib
import os

# Get email credentials and other information from environment variables
from_email = os.environ.get('EMAIL_USERNAME')
password = os.environ.get('EMAIL_PASSWORD')
to_email = os.environ.get('TO_EMAIL')
message = os.environ.get('MESSAGE')


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(from_email, password)
server.sendmail(from_email, to_email, message)
server.rset()
server.quit()
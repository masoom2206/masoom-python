# All imports below are part of python built packages no need to install any exras

# smtplib provides functionality to send emails using SMTP.
import smtplib
# MIMEMultipart send emails with both text content and attachments.
from email.mime.multipart import MIMEMultipart
# MIMEText for creating body of the email message.
from email.mime.text import MIMEText
# MIMEApplication attaching application-specific data (like CSV files) to email messages.
from email.mime.application import MIMEApplication

from string import Template
from pathlib import Path

# subject = 'Fourth mail from Python Script with attachment!'
# sender_email = 'masoom2206@gmail.com'
# recipient_email = 'masoom.haider@axelerant.com'
# sender_password = 'ykre tkqz skis qkap'
# smtp_server = 'smtp.gmail.com'
# smtp_port = 465
# path_to_file = 'Learning/Udemy/Scripting/EmailProcess/pikachu.jpg'
# body = "This is the body of the text message with attachment."


# # MIMEMultipart() creates a container for an email message that can hold
# # different parts, like text and attachments and in next line we are
# # attaching different parts to email container like subject and others.
# message = MIMEMultipart()
# message['Subject'] = subject
# message['From'] = sender_email
# message['To'] = recipient_email
# body_part = MIMEText(body)
# message.attach(body_part)

# # section 1 to attach file
# with open(path_to_file,'rb') as file:
#   # Attach the file with filename to the email
#   message.attach(MIMEApplication(file.read(), Name="pikachu.jpg"))

# # secction 2 for sending email
# with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
#   server.login(sender_email, sender_password)
#   server.sendmail(sender_email, recipient_email, message.as_string())
# print("Message delivered with attachment successfully!")


# ------------------------------------------------------------------

# The html content mail with attachment

html = Template(Path('Learning/Udemy/Scripting/EmailProcess/mail.html').read_text())

email = MIMEMultipart()

email['from'] = "MasoomGmail 2206"
email['to'] = 'masoom.haider@axelerant.com'
email['subject'] = 'Fifth mail from Python Script!'
body = html.substitute({'name': "Haider", 'address': 'Delhi'})
body_part = MIMEText(body, 'html')
email.attach(body_part)

path_to_file = 'Learning/Udemy/Scripting/ImageProcess/Pokedesk/bulbasaur.jpg'
# section 1 to attach file
with open(path_to_file,'rb') as file:
  # Attach the file with filename to the email
  email.attach(MIMEApplication(file.read(), Name="pikachu.jpg"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  email_address = 'masoom2206@gmail.com'
  email_password = 'ykre tkqz skis qkap'
  smtp.login(email_address, email_password)
  smtp.send_message(email)
  print("HTML email delivered with attachment successfully!")


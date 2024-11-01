import smtplib
from email.message import EmailMessage
# The html content mail
from string import Template
from pathlib import Path

# email = EmailMessage()

# email['from'] = "MasoomGmail 2206"
# email['to'] = 'masoom.haider@axelerant.com'
# email['subject'] = 'New mail from Python Script!'

# email.set_content(f"Hello\nI am Masoom\nI am using Python script to send this mail.")

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#   smtp.ehlo()
#   smtp.starttls()
#   email_address = 'masoom2206@gmail.com'
#   email_password = 'ykre tkqz skis qkap'
#   smtp.login(email_address, email_password)
#   smtp.send_message(email)
#   print("Message delivered successfully!")

# ------------------------------------------------------------------

# The html content mail

html = Template(Path('Learning/Udemy/Scripting/EmailProcess/mail.html').read_text())

email = EmailMessage()

email['from'] = "MasoomGmail 2206"
email['to'] = 'masoom.haider@axelerant.com'
email['subject'] = 'Second mail from Python Script!'

email.set_content(html.substitute({'name': "Haider", 'address': 'Delhi'}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  email_address = 'masoom2206@gmail.com'
  email_password = 'ykre tkqz skis qkap'
  smtp.login(email_address, email_password)
  smtp.send_message(email)
  print("Message delivered successfully!")

# twilio use to send SMS, audio and video

from twilio.rest import Client

asid = 'XXX'
atoken = 'XXX'
client = Client(asid, atoken)
message = client.messages.create(
  from_='+000',
  body='Hello Masoom, sending SMS from Python code',
  to='+000'
)
print(message.sid)
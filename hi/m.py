import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC0a8bc0cf83968ec3b15db72e7febd2b0"
auth_token = "8cda4665733f44da2eda29482af14f67"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+918696316302",
  from_="+15182914865"
)

print(call.sid)
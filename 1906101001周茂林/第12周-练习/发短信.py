# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc21a491399bf08fcb7b29779f980c8e5'
auth_token = '4f724ec7aed71afbaaacc99c5c401023'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hi,boy!",
                     from_='+12562448228',
                     to='+8617738050158'
                 )

print(message.sid)
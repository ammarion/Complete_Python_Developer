# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = "AC50"
auth_token = "b3ecb54a"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+16193206172",
    to="+12064889803",
)

print(message.sid)

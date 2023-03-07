from twilio.rest import Client
# Your Account Sid and Auth Token from twilio.com/console

account_sid = 'ACb65458640a21683e8bcbe8599e791636'
auth_token = "a534c69753732de82a5508670b6a9eea"
# Define sid and token

client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+15673392292",
  to="+84984526993"
)
# Create message

print(message.sid)
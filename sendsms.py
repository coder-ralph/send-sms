# importing twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com / console
account_sid = 'insert your sid here'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

''' Change the value of 'from' with the number
received from Twilio and the value of 'to'
with the number in which you want to send message.'''
message = client.messages.create(
							from_='+63987654321',
							body ='body',
							to ='+63987654321'
						)

print(message.sid)
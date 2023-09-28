import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>hello ajeeta!</Say></Response>',
                        to='+919467389160',
                        from_='+918708115075'
                    )

print(call.sid)
print(call)


# from twilio.rest import Client
# from twilio.base.exceptions import TwilioRestException



# try:
#   # This could potentially throw an exception!
#   message = client.messages.create(
#     to="+919467389160", 
#     from_="+918708115075",
#     body="Hello there!")
# except TwilioRestException as err:
#   # Implement your fallback code here
#   print(err)
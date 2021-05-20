# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACe54d2a420b0fae79fd7bc4c08fff3b35'
    auth_token = '6a39ef1540191dfc1ef39bb0ffdb1626'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+13179342053',
                        to='+'+to
                    )

    print(message.sid)
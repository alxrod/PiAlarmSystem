from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC2cc4c08fab15b4a7ac6717a6a66fa3a6"
auth_token = "126df82c59b94219fe0b3294498b1936"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+16173010887",
    from_="+16178700118",
    body="Hello there!")

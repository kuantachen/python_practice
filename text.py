from email import message
from http import client
from multiprocessing.connection import Client


from twilio.rest import Client

account_sid = "AC62bf3787f8d3b66a08f4f08bf747ce33"

auth_token = "a9f41661975820bdf8519eeb564da6eb"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+886985666898",
    from_="+12057496335",
    body="大家好這是個 Python code 測試！"
)

print(message.sid)
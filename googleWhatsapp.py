from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('message') is None:
        message = "Salut"
    else:
        message = request.args.get('message')

    client = Client('', '')
    whMessage = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to='whatsapp:+')
    return "Message envoyé"


if __name__ == '__main__':
    app.run(debug=False)

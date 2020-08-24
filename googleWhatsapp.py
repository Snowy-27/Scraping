from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.get('message') is None:
        message = "Salut"
    else:
        message = request.args.get('message')

    client = Client('AC57e474a2839a87536a6c91ce495e5fa1', '16f9168155d0e2bbf463feb7c749e5b0')
    whMessage = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message,
        to='whatsapp:+33651598405')
    return "Message envoyé"


if __name__ == '__main__':
    app.run(debug=False)

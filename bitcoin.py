import time
from bs4 import BeautifulSoup
from selenium import webdriver
from twilio.rest import Client

class WhatsappBitcoin:
    def __init__(self, account_sid, auth_token, hidden=False, dan=""):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.hidden = hidden
        self.message = ""
        self.counter = 1
        self.dan = dan

    def getBitcoin(self):
        # recuper le prix
        if self.hidden:
            op = webdriver.ChromeOptions()
            op.add_argument('headless')
            driver = webdriver.Chrome(options=op)
        else:
            driver = webdriver.Chrome()
        driver.get('https://bitcoin.fr/le-cours-du-bitcoin/')
        time.sleep(2)
        page = driver.page_source
        driver.close()
        soup = BeautifulSoup(page, 'lxml')
        price = soup.find_all('span', {'class': 'pcw-field pcw-field-price'})
        self.message = f"Voici le prix du bitcoin: \nPrix en euro: {price[0].text}€\nPrix en dollar: {price[2].text}$"
        client = Client(self.account_sid, self.auth_token)
        whMessage = client.messages.create(
            from_='whatsapp:+14155238886',
            body=self.message,
            to='whatsapp:+3333333333')
        if self.counter < 2:
            print(str(self.counter) + " message!")
        else:
            print(str(self.counter) + " messages!")
        self.counter += 1



import requests
from bs4 import BeautifulSoup as scrap
import time
import os
from flask import Flask
app = Flask(__name__)
os.system('cls')


def BrawlStats():
    response = requests.get(f'https://www.starlist.pro/stats/profile/quuvc')
    soup = scrap(response.text, 'lxml')
    trophies = soup.find(
        'td', {'class': "text-left shadow-normal text-warning"}
    ).text
    trophies = int(trophies.replace(',', ''))
    highesttrophies = soup.find(
        'td', {'class': "text-left text-hp2 shadow-normal"}
    ).text
    highesttrophies = highesttrophies.replace(',', '')

    return ("Trophies: " + str(trophies) + "<br> Highest Trophies: " + highesttrophies)


# tag = str(input('Entrer votre tag: '))


@app.route('/')
def hello_world():
    return BrawlStats()


app.run(host='192.168.1.140',  port=5000)

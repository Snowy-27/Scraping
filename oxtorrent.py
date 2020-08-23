from bs4 import BeautifulSoup as scrap
import requests
import time
import schedule
from fp.fp import FreeProxy
proxy = FreeProxy().get()
list = []
counter = 1


def ScrapTorrent():
    global counter
    print(counter)
    counter += 1
    url = 'https://www.oxtorrent.cc/'
    response = requests.get(url, proxy=proxy)
    soup = scrap(response.text, 'lxml')
    table = soup.findAll('table', {'class': 'table table-hover'})
    for i in range(0, 7):
        for item in table[i].findAll('a'):
            list.append(item.text)
        if i == 0:
            print('Films : ')
        elif i == 1:
            print('Series : ')
        elif i == 2:
            print('Musiques : ')
        elif i == 3:
            print('Jeux pc  : ')
        elif i == 4:
            print('Jeux consoles : ')
        elif i == 5:
            print('Logiciels : ')
        elif i == 6:
            print('Ebook : ')
        for ite in list:
            print(ite)
        list.clear()
        print('-----------------------------------------------------')


ScrapTorrent()
schedule.every(5).seconds.do(ScrapTorrent)
while True:
    schedule.run_pending()
    time.sleep(1)

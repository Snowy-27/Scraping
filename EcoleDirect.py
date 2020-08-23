from selenium import webdriver
from bs4 import BeautifulSoup
import time
class EcoleDirect:
    def __init__(self, username, password, hidden=False):
        self.username = username
        self.password = password
        self.hidden = hidden

    def EcoleDirectScraping(self):
        if self.hidden:
            op = webdriver.ChromeOptions()
            op.add_argument('headless')
            driver = webdriver.Chrome(options=op)
        else:
            driver = webdriver.Chrome()
        driver.get('https://www.ecoledirecte.com/login')
        nameInput = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[1]')
        passInput = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/input[2]')
        nameInput.send_keys('danhabib')
        passInput.send_keys('D27032005h')
        button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[3]/form/button')
        button.click()
        time.sleep(2)
        info = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/ed-menu[1]/div/div/ul/li[2]/a')
        info.click()
        time.sleep(2)
        page_source = driver.page_source
        emails = [driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/ng-include/form/div[2]/div[1]/div/div/div[4]/div/span'),
                  driver.find_element_by_xpath(
                      '/html/body/div[2]/div[2]/div[2]/div/div[1]/div[1]/ng-include/form/div[2]/div[2]/div/div/div[4]/div/span')]
        for i in range(0, 2):
            print(emails[i].get_attribute('innerHTML'))
        driver.quit()
        soup = BeautifulSoup(page_source, 'lxml')
        adresse = soup.find_all('span', {'class': 'inputvalue'})
        print(adresse[0].text.replace(',', ''))


user = EcoleDirect("danhabib", 'D27032005h', False)
user.EcoleDirectScraping()

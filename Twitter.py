from selenium import webdriver
import time


class Twitter:
    def __init__(self, username, password, tweet, hidden = False):
        self.username = username
        self.password = password
        self.tweet = tweet
        self.hidden = hidden


    def Tweet(self):
        if self.hidden:
            op = webdriver.ChromeOptions()
            op.add_argument('headless')
            driver = webdriver.Chrome(options=op)
        else:
            driver = webdriver.Chrome()
        url = 'https://twitter.com/login'
        driver.get(url)
        userInput = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        passInput = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        userInput.send_keys(self.username)
        passInput.send_keys(self.password)
        buttonLogin = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div').click()
        tweetButton = driver.find_element_by_xpath(
            "/html/body/div/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div").click()
        inputTweet = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys(
            self.tweet)
        ConfirmButton = driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]/div').click()
        time.sleep(2)
        driver.close()

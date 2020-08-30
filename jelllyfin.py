from selenium import webdriver
import time
import schedule

i = 1


def refreshJellyfin():
    global i
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)
    driver.get('http://77.133.245.248:8096/')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[2]/input').send_keys('snowy-27')
    driver.find_element_by_xpath('/html/body/div[5]/div/div/form/button').click()
    time.sleep(1)
    driver.get('http://77.133.245.248:8096/web/index.html#!/library.html')
    driver.refresh()
    time.sleep(1)
    refresh = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/button')
    refresh.click()
    time.sleep(3)
    driver.close()
    print('refresh ' + str(i))
    i += 1


schedule.every(1).minute.do(refreshJellyfin)

while True:
    schedule.run_pending()
    time.sleep(1)

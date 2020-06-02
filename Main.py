from selenium import webdriver
from selenium import webdriver, common
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.proxy import *


browser = webdriver.Firefox()
browser.set_window_size(1920, 1080)


browser.get('https://ru.tradingview.com/chart/?symbol=MOEX%3AEURUSD_TOM')
time.sleep(2)

while 1:
    try:
        browser.find_element_by_css_selector('.tv-spinner').click()
    except:
        break
time.sleep(2)

browser.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[2]/div/div/div/div/div[3]').click()
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[3]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div/div[3]/div[2]').click()
time.sleep(1)
ActionChains(browser).move_to_element(browser.find_element_by_xpath('/html/body/div[2]/div[5]/div/div[2]/div/div/div/div/div[3]')).perform()
time.sleep(1)


dataAndTime = browser.find_element_by_css_selector('.box:nth-child(1) > .chart-data-window-body').text
valueElem = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[5]').text
print(dataAndTime)


oldDateAndTime = dataAndTime
while oldDateAndTime == dataAndTime:
    dataAndTime = browser.find_element_by_css_selector('.box:nth-child(1) > .chart-data-window-body').text
    ActionChains(browser).move_by_offset(-10, 0).perform()

print(dataAndTime)

information = []

dataAndTime = browser.find_element_by_css_selector('.box:nth-child(1) > .chart-data-window-body').text
dataAndTime = dataAndTime[dataAndTime.find('\n') + 6:]
dataAndTime = time.strptime(dataAndTime + " 2020", "%H:%M %Y")
dataAndTime = float(time.mktime(dataAndTime))
oldDataAndTime = dataAndTime
while 1:
    try:
        ActionChains(browser).move_by_offset(-2, 0).perform()
    except:
        try:
            ActionChains(browser).move_by_offset(2, 0).perform()
        except:
            pass
        break

    try:
        value = browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div[5]').text.split(' ')[1][1:-2].replace('−', '-')
        dataAndTime = browser.find_element_by_css_selector('.box:nth-child(1) > .chart-data-window-body').text
        dataAndTime = dataAndTime[dataAndTime.find('\n') + 6:]
        dataAndTime = time.strptime(dataAndTime + " 2020", "%H:%M %Y")
        dataAndTime = float(time.mktime(dataAndTime))
    except:
        continue
    try:
        if float(dataAndTime) != oldDataAndTime:
            oldDataAndTime = dataAndTime
            information += [[float(value), dataAndTime]]
            print(information)
    except ValueError:
        break

information.reverse()
print(information)
print("Сканирование закончено")
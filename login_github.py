from selenium import webdriver
from time import sleep
import os
Id=os.environ.get('GH_ID').replace('dummy','')
Pw=os.environ.get('GH_PW').replace('dummy','')
browser = webdriver.Chrome('C:\\Users\\user\\python\\web_scraping\\driver\\chromedriver')
loginUrl= "https://github.com/login"
browser.get(loginUrl)
elem_username=browser.find_element_by_name('login')
elem_username.send_keys(Id)
sleep(1)
elem_username=browser.find_element_by_name('password')
elem_username.send_keys(Pw)
sleep(1)
elem_login_btn=  browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[13]')
elem_login_btn.click()
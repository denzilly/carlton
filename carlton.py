from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from random import *
import csv
import os
import time

from bs4 import BeautifulSoup
import requests


driver = webdriver.Firefox()
driver.get("https://www.rtvutrecht.nl/formulier/top100/")



###########List of XPaths#############
cookie   = "/html/body/app-root/app-theme/div/div/app-home/div/div/div[2]/div[2]/div[2]/div[2]/button/span/b"
name     = "/html/body/div[2]/main/div/div/section/article/form/div[1]/div/input"
address  =   "/html/body/div[2]/main/div/div/section/article/form/div[2]/div/input"
postcode =  "/html/body/div[2]/main/div/div/section/article/form/div[3]/div/input"
city     = "/html/body/div[2]/main/div/div/section/article/form/div[4]/div/input"
phone    = "/html/body/div[2]/main/div/div/section/article/form/div[5]/div/input"
email    = "/html/body/div[2]/main/div/div/section/article/form/div[6]/div/input"
choice   = "/html/body/div[2]/main/div/div/section/article/form/div[7]/div/div/select"
captcha  = "//*[@id=\"code\"]"


###########Email Generator##############

def getmail():
    r = requests.get("https://www.10minutemail.com", timeout=5)

    pc = BeautifulSoup(r.content, "html.parser")

    email = pc.find("input", {"id": "mailAddress"}).get('value')

    return email



##############Name, Place, and Phone###########

#Generate name (GLenn is doing)


#Generate an address



#Generate random phone number

phone_no = "064" + str(randint(1000000,9999999))


############### Entering information ##############

def enter(field,text):
    driver.find_element_by_xpath(field).send_keys(text)

dropdown = Select(driver.find_element_by_xpath(choice))


time.sleep(3)
enter(name, "Bill Johson")
enter(address, "Bill street")
enter(postcode, "6222AH")
enter(city, "Maastricht")
enter(phone, phone_no)
enter(email,getmail())


dropdown.select_by_value('23070')

print("should be done")

time.sleep(3)
driver.close()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import stem.process
from stem import Signal
from stem.control import Controller
from splinter import Browser




import time



from captcha import solve_captcha
from generator import get_phone, get_name_email, get_address

import pyscreenshot as ImageGrab
from PIL import Image




########## TOR PROXY SETTINGS ###############
#Shit is getting a little complicated, but we are pressed for time

ffprofile = webdriver.FirefoxProfile()

proxyIP = "127.0.0.1"
proxyPort = 9150

ffprofile.set_preference("network.proxy.type", 1)
ffprofile.set_preference("network.proxy.ssl", proxyIP)
ffprofile.set_preference("network.proxy.ssl_port", proxyPort)
ffprofile.set_preference("network.proxy.socks", proxyIP)
ffprofile.set_preference("network.proxy.socks_port", proxyPort)
ffprofile.set_preference("network.proxy.socks_remote_dns", True)
ffprofile.set_preference("network.proxy.ftp_port", proxyPort)
ffprofile.set_preference("network.proxy.ftp", proxyIP)








def switchIP():
	with Controller.from_port(port=9151) as controller:
		controller.authenticate()
		controller.signal(Signal.NEWNYM)


switchIP()

###########List of XPaths#############
cookie   = "/html/body/app-root/app-theme/div/div/app-home/div/div/div[2]/div[2]/div[2]/div[2]/button/span/b"
cookie2  = "/html/body/app-root/app-theme/div/div/app-home/div/div/div[2]/div[2]/div[2]/div[2]"


name_field     = "/html/body/div[2]/main/div/div/section/article/form/div[1]/div/input"
address_field  =   "/html/body/div[2]/main/div/div/section/article/form/div[2]/div/input"
postcode_field =  "/html/body/div[2]/main/div/div/section/article/form/div[3]/div/input"
city_field     = "/html/body/div[2]/main/div/div/section/article/form/div[4]/div/input"
phone_field    = "/html/body/div[2]/main/div/div/section/article/form/div[5]/div/input"
email_field    = "/html/body/div[2]/main/div/div/section/article/form/div[6]/div/input"

name_field2     = "/html/body/div[1]/main/div/div/section/article/form/div[1]/div/input"
address_field2  =   "/html/body/div[1]/main/div/div/section/article/form/div[2]/div/input"
postcode_field2 =  "/html/body/div[1]/main/div/div/section/article/form/div[3]/div/input"
city_field2     = "/html/body/div[1]/main/div/div/section/article/form/div[4]/div/input"
phone_field2    = "/html/body/div[1]/main/div/div/section/article/form/div[5]/div/input"
email_field2    = "/html/body/div[1]/main/div/div/section/article/form/div[6]/div/input"


choice_field   = "/html/body/div[2]/main/div/div/section/article/form/div[7]/div/div/select"
choice_field2  = "/html/body/div[1]/main/div/div/section/article/form/div[7]/div/div/select"


captcha_field  = "//*[@id=\"code\"]"
captcha_field2 = "//*[@id=\"code\"]"

send = "/html/body/div[2]/main/div/div/section/article/form/div[11]/div/button"
send2 = "/html/body/div[1]/main/div/div/section/article/form/div[11]/div/button"


###########Get Personal Information################

phone = get_phone()
name_mail = get_name_email()
address = get_address()


################### CAPTCHA ##################


print("#####    Who are you today, Carlton?   #####")
print(phone)
print(name_mail)
print(address)



############### Entering information ##############

driver = webdriver.Firefox(ffprofile)
driver.get("https://www.rtvutrecht.nl/formulier/top100/")





##### Collect Captcha Slices
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(3)
#driver.find_element_by_xpath(cookie2).click()

time.sleep(1)


im = ImageGrab.grab(bbox=(661,487,709,505)).convert('RGB')

im.save("captcha_full.png")
bg = Image.open("data/resources/bg.png").convert('LA')


for x in range (1,7):
    x_bound = (x-1) * 8

    crop = im.crop((x_bound,0,x_bound + 8,18))
    name = "slice_" + str(x) + ".png"
    #print(name)

    back_im = bg.copy()
    back_im.paste(crop, (10,5))
    back_im.save("data/captcha_slices/" + name)



captcha = solve_captcha()





def enter(field,text):
    driver.find_element_by_xpath(field).send_keys(text)

try:
    dropdown = Select(driver.find_element_by_xpath(choice_field2))
except NoSuchElementException:
    dropdown = Select(driver.find_element_by_xpath(choice_field))

time.sleep(3)

try:
    enter(name_field, name_mail[0])
    enter(address_field, address[0])
    enter(postcode_field, address[1])
    enter(city_field, address[2])
    enter(phone_field, phone)
    enter(email_field, name_mail[1])
    enter(captcha_field, captcha)

except NoSuchElementException:
    enter(name_field2, name_mail[0])
    enter(address_field2, address[0])
    enter(postcode_field2, address[1])
    enter(city_field2, address[2])
    enter(phone_field2, phone)
    enter(email_field2, name_mail[1])
    enter(captcha_field, captcha)

dropdown.select_by_value('23070')

time.sleep(0.5)


try:
    driver.find_element_by_xpath(send2).click()
except NoSuchElementException:
    driver.find_element_by_xpath(send).click()


print("Vote Sent")

time.sleep(3)
#driver.close()

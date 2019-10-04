
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get("https://www.rtvutrecht.nl/formulier/top100/")



##### Collect Captcha Slices
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 500)")

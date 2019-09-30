import pyscreenshot as ImageGrab
import time
from selenium import webdriver
import image_slicer
from PIL import Image



options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")



driver = webdriver.Firefox(firefox_options=options)
driver.get("https://www.rtvutrecht.nl/formulier/top100/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 500)")


time.sleep(1)

bound_laptop = "nothing"
bound_desktop = (2337,520,2385,538)

im = ImageGrab.grab(bbox=(2337,520,2385,538)).convert('LA')

im.save("captcha_full.png")
bg = Image.open("bg.png").convert('LA')


for x in range (1,7):
    x_bound = (x-1) * 8

    crop = im.crop((x_bound,0,x_bound + 8,18))
    name = "slice_" + str(x) + ".png"
    print(name)

    back_im = bg.copy()
    back_im.paste(crop, (10,5))
    back_im.save(name)


#driver.close()

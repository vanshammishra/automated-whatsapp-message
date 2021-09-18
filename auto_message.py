import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(10)
# input("Please scan the QR code and enter any key")
siddhartha = driver.find_element_by_css_selector('span[title="Diksha Mami"]')
siddhartha.click()
db = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]")
time.sleep(7)
db.send_keys("https://dchgfmkorsq")
db.send_keys(Keys.RETURN)

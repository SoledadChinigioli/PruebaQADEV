import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:/Users/mchinigi/chromedriver.exe"
URL = "https://www.google.com/"
SEARCH_WORD = "automatización"
URL_SCREENSHOT="C:/Users/mchinigi/Documents/Prueba Técnica de Test/SeleniumTest/automatization.png"


driver = webdriver.Chrome(PATH)

driver.get(URL)
driver.maximize_window()
find_cookies_button = driver.find_element(By.XPATH,"//*[(text()='Rechazar todo')]")
find_cookies_button.click()
time.sleep(1)
search_input = driver.find_element(By.XPATH,"//*[@title='Buscar']")
search_input.send_keys(SEARCH_WORD)
search_input.send_keys(Keys.RETURN)
find_wikipedia_link = driver.find_element(By.XPATH,"//*[contains(@href,'wikipedia')]//h3[contains(text(),'Automatización')]")
find_wikipedia_link.click()
find_first_automated_process_year = driver.find_element(By.XPATH,"//p[contains(.,'primer proceso')]")
find_first_automated_process_year.click()
print(find_first_automated_process_year.text)
driver.save_screenshot(URL_SCREENSHOT)


driver.quit()
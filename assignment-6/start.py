from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.ChromiumEdge()
driver.get("https://play2048.co/")

COOKIE_BUTTON_XPATH = '//*[@id="ez-accept-all"]'
ADVERTISMENT_BUTTON_XPATH = '//*[@id="ezmob-footer-close"]'

cookies_button = driver.find_element(By.XPATH, COOKIE_BUTTON_XPATH)
cookies_button.click()

ads_button = driver.find_element(By.XPATH, ADVERTISMENT_BUTTON_XPATH)
ads_button.click()

time.sleep(100)
driver.close()
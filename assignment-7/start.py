from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.ChromiumEdge()
driver.get("https://play2048.co/")

COOKIE_BUTTON_XPATH = '//*[@id="ez-accept-all"]'
ADVERTISMENT_BUTTON_XPATH = '//*[@id="ezmob-footer-close"]'
GAME_OVER_DIALOG_XPATH = '/html/body/div[2]/div[3]/div[1]/p'

cookies_button = driver.find_element(By.XPATH, COOKIE_BUTTON_XPATH)
cookies_button.click()

ads_button = driver.find_element(By.XPATH, ADVERTISMENT_BUTTON_XPATH)
ads_button.click()

action = ActionChains(driver)

while (True):
    element = driver.find_element(By.XPATH, GAME_OVER_DIALOG_XPATH)

    if element.text == 'Game over!':
        print(f"Game over!")
        break

    action.send_keys(Keys.ARROW_LEFT).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_RIGHT).perform()
    action.send_keys(Keys.ARROW_UP).perform()



driver.close()
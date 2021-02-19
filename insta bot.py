from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import re
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')   ## connecting to instagram

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']"))) 
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']"))) 

username.clear()
password.clear()

username.send_keys('username')
password.send_keys('password')

log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[type='submit']"))).click() 
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
#notification = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()

driver.get("https://www.instagram.com/username/")
following = driver.find_element_by_partial_link_text('following')
following.click()
sleep(5)

for i in range(45):
    driver.find_element_by_xpath("//button[contains(text(),'Following')]").click()
    driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]").click()
    sleep(2)
    
driver.quit()
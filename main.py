import time
from logg import vk_pass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = chrome_options()

driver = webdriver.Chrome(executable_path='C:\Program Files\Google\chromedriver.exe', options=options)

url = 'https://vk.com/'
driver.get(url)
elem = driver.find_element(By.CLASS_NAME, "VkIdForm__input")
time.sleep(2)
print(elem)
elem.send_keys('89513651398')
time.sleep(2)
elem.send_keys(Keys.ENTER)
time.sleep(15)
login = driver.find_element(By.NAME, "password")
print(login)
login.send_keys(vk_pass)
time.sleep(3)
login.send_keys(Keys.ENTER)
time.sleep(10)
music = driver.find_element(By.ID, "l_aud")
music.click()
time.sleep(5)
my_music = driver.find_element(By.CLASS_NAME, "_audio_section_tab__all")
my_music.click()
time.sleep(5)
track = driver.find_element(By.CLASS_NAME,"audio_page_player_icon")
track.click()
time.sleep(36)
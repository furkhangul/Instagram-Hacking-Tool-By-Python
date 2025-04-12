#Bu prototip başarısızlıkla sonuçlanmıştır...
#FurOfTheWeak | Furkan Gül


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getUser import username,password
import time

class Instagram():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def kullaniciGiris(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(7)
        self.driver.find_element(By.NAME, 'username')
        self.driver.find_element(By.NAME, 'password')
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(7)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

instgrm = Instagram(username,password)
instgrm.kullaniciGiris()

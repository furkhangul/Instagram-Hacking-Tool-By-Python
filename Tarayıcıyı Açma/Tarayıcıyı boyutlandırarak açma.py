from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Gecko WebDriver'ın dosya yolunu belirtin
webdriver_path = "C:/Users/Furkan/Desktop/geckodriver.exe"

# WebDriver'ı başlatın
driver = webdriver.Firefox()
driver.set_window_position(0, 0)
driver.set_window_size(100, 100)
driver.get("https://www.google.com")

# Google arama kutusunu bulun ve arama yapın
search_box = driver.find_element_by_name("q")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

# Sayfayı kapatın
driver.quit()

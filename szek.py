from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.ikea.com/hu/hu/p/jaervfjaellet-irodai-szek-karfakkal-gunnared-sszuerke-fekete-s99275632/")


driver.implicitly_wait(10)

link = driver.find_element_by_link_text("Áruházi készlet ellenőrzése")
link.click()

driver.find_element_by_class_name("range-revamp-stockcheck__store-text")
status = driver.find_element_by_class_name('range-revamp-stockcheck__store-text')

print(status.text)

driver.quit()
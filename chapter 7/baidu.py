from selenium import webdriver
import time


driver = webdriver.Chrome()

# driver = selenium.webdriver.Firefox()
# 

driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

time.sleep(5)

driver.quit()
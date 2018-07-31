# -*- coding: utf-8 -*-：
from selenium import webdriver
import time
driver = webdriver.Firefox(executable_path="F:\\driver\\geckodriver")
driver.get("http://www.sogou.com")
driver.find_element_by_id('query').clear()
driver.find_element_by_id('query').send_keys(u"光荣之路自化测试")
driver.find_element_by_id('stb').click()
time.sleep(3)
driver.quit()

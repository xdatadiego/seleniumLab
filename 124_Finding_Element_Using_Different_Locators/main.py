import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.ID, "ta1").send_keys("My name is Diego")

driver.find_element(By.NAME, "q").send_keys("My name is Diego")
time.sleep(5)

driver.find_element(By.CLASS_NAME, "dropbtn").click()
time.sleep(3)

# ~ driver.find_element(By.LINK_TEXT, "compendiumdev").click()

driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)

driver.quit()
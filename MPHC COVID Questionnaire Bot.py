from selenium import webdriver 
from selenium.webdriver.support.ui import Select 
import config

# Personal details go in config.py file

driver = webdriver.Chrome()
driver.get(config.URL)
driver.implicitly_wait(3)

try:
    # Page 1
    driver.find_element_by_css_selector("#myself > div").click()
    driver.find_element_by_css_selector("#continueButton").click()
    driver.implicitly_wait(3)
except Exception as e:
    pass

# Page 2

month, day, year = config.DOB.split('-')
try:
    driver.find_element_by_css_selector("#legalFirstName").send_keys(config.NAME_FIRST)
    driver.implicitly_wait(0.5)
    driver.find_element_by_css_selector("#lastName").send_keys(config.NAME_LAST)
    driver.implicitly_wait(0.5)
    driver.find_element_by_css_selector("#phoneNumber").send_keys(config.PHONE)
    driver.implicitly_wait(0.5)
    Select(driver.find_element_by_css_selector("#myselfMonth")).select_by_value(str(int(month)-1))
    Select(driver.find_element_by_css_selector("#myselfDay")).select_by_value(str(int(day)))
    Select(driver.find_element_by_css_selector("#myselfYear")).select_by_value(year)
    driver.find_element_by_css_selector("#email").send_keys(config.EMAIL)
    driver.find_element_by_css_selector("#checkbox-Have-you-a--myself-1-1").click()
    driver.find_element_by_css_selector("#checkbox-Have-you-b--myself-1-1").click()
    driver.find_element_by_css_selector("#checkbox-Have-you-c--myself-1-1").click()
    driver.find_element_by_css_selector("#checkbox-Have-you-d--myself-1-1").click()
    driver.implicitly_wait(0.5)
    submit_btn = driver.find_element_by_css_selector("#nextButton")
    driver.execute_script("arguments[0].click();", submit_btn)
except Exception as e:
    print(e)

# Page 3
try:
    driver.find_element_by_css_selector("#beginSigningButton").click()
    driver.implicitly_wait(1)
except:
    pass

# Page 4
submit_btn = driver.find_element_by_css_selector("#adultApplySignature-label")
driver.execute_script("arguments[0].click();", submit_btn)
driver.implicitly_wait(1)
driver.find_element_by_css_selector("#agreeAndSubmitButton").click()

# Teardown
driver.quit()

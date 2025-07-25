from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

# Use correct field IDs as per the site's HTML
driver.find_element(By.ID, "firstname").send_keys("John")
driver.find_element(By.ID, "lastname").send_keys("Doe")
driver.find_element(By.ID, "email_address").send_keys("john.doe12346@example.com")  # Use new email every time
driver.find_element(By.ID, "password").send_keys("Test@1234")
driver.find_element(By.ID, "password-confirmation").send_keys("Test@1234")

# Click the Create Account button
driver.find_element(By.CSS_SELECTOR, "button[title='Create an Account']").click()

# Wait to observe result
time.sleep(5)
driver.quit()


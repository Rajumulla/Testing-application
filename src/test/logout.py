from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start browser
driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

# Login
driver.find_element(By.ID, "email").send_keys("john.doe12346@example.com")
driver.find_element(By.ID, "pass").send_keys("Test@1234")
driver.find_element(By.ID, "send2").click()

# Wait for "Welcome, John Doe!" dropdown to appear
welcome = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "customer-welcome"))
)

# Click the "Welcome, John Doe!" to expand dropdown
welcome.click()

# Wait for "Sign Out" link and click it
sign_out = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out"))
)
sign_out.click()

# Wait for logout to complete
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Sign In"))
)

print(" Logged out successfully.")
driver.quit()


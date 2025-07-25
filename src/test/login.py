from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Setup browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

# Step 2: Login with registered credentials
driver.find_element(By.ID, "email").send_keys("john.doe12346@example.com")
driver.find_element(By.ID, "pass").send_keys("Test@1234")
driver.find_element(By.ID, "send2").click()

# Step 3: Wait for dashboard and click 'Change Password' from left menu
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, "Change Password"))
)
driver.find_element(By.LINK_TEXT, "Change Password").click()

# Step 4: Wait for the fields to load and fill in the password change form
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "current-password"))
)

driver.find_element(By.ID, "current-password").send_keys("Test@1234")      # current password
driver.find_element(By.ID, "password").send_keys("Test@5678")              # new password
driver.find_element(By.ID, "password-confirmation").send_keys("Test@5678") # confirm password

# Step 5: Click Save button
driver.find_element(By.CSS_SELECTOR, "button.save.primary").click()

# Step 6: Optional wait and quit
time.sleep(5)
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set your existing login credentials here
EMAIL = "john.doe12346@example.com"
OLD_PASSWORD = "Test@1234"
NEW_PASSWORD = "Test@12345"

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Open login page
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

    # Step 2: Enter email and password
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(EMAIL)
    driver.find_element(By.ID, "pass").send_keys(OLD_PASSWORD)
    driver.find_element(By.ID, "send2").click()

    # Step 3: Wait for successful login
    time.sleep(3)

    # Step 4: Click on the profile name (top right corner)
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='logged-in']"))).click()

    # Step 5: Click 'My Account'
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My Account"))).click()

    # Step 6: Click 'Change Password' from the side menu
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Change Password"))).click()

    # Step 7: Wait and fill in password fields
    wait.until(EC.presence_of_element_located((By.ID, "current-password"))).send_keys(OLD_PASSWORD)
    driver.find_element(By.ID, "password").send_keys(NEW_PASSWORD)
    driver.find_element(By.ID, "password-confirmation").send_keys(NEW_PASSWORD)

    # Step 8: Click Save
    driver.find_element(By.XPATH, "//button[@title='Save']").click()

    # Step 9: Wait and verify success
    success_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "message-success")))
    print("✅ Password changed successfully!")

except Exception as e:
    print("❌ Error:", e)

finally:
    time.sleep(5)
    driver.quit()

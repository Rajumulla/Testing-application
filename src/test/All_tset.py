from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Reusable email and password
email = "Subanitest123@example.com"  # your static email
password = "Test@1234"
new_password = "Test@5678"

# Setup driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/")

# Helper: Wait for element by ID
def wait_and_get(by, value, timeout=10):
    for _ in range(timeout):
        try:
            return driver.find_element(by, value)
        except:
            time.sleep(1)
    raise Exception(f"Element not found: {value}")

# Sign Up (only if needed)
def signup():
    driver.find_element(By.LINK_TEXT, "Create an Account").click()
    time.sleep(2)
    driver.find_element(By.ID, "firstname").send_keys("Yogesh")
    driver.find_element(By.ID, "lastname").send_keys("Test")
    driver.find_element(By.ID, "email_address").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password-confirmation").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[title='Create an Account']").click()
    time.sleep(4)
    print("✅ Account created.")

# Logout
def logout():
    driver.find_element(By.CSS_SELECTOR, "button[data-action='customer-menu-toggle']").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Sign Out").click()
    time.sleep(4)
    print("✅ Logged out.")

# Login
def login():
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    wait_and_get(By.ID, "email").send_keys(email)
    wait_and_get(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()
    time.sleep(4)
    print("✅ Logged in.")

# Change Password
def change_password(old_pass, new_pass):
    # Go to My Account
    driver.find_element(By.CSS_SELECTOR, "button[data-action='customer-menu-toggle']").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "My Account").click()
    time.sleep(3)

    # Click Change Password in sidebar
    driver.find_element(By.LINK_TEXT, "Change Password").click()
    time.sleep(2)

    # Fill and Save
    driver.find_element(By.ID, "current-password").send_keys(old_pass)
    driver.find_element(By.ID, "password").send_keys(new_pass)
    driver.find_element(By.ID, "password-confirmation").send_keys(new_pass)
    driver.find_element(By.CSS_SELECTOR, "button[title='Save']").click()
    time.sleep(3)
    print("✅ Password changed.")

# ✅ Execute all cases
try:
    signup()
    logout()
    login()
    change_password(password, new_password)
    logout()
    password = new_password  # Update password for future login
    login()
    print("✅ Final login with new password successful.")
except Exception as e:
    print("❌ Error:", e)
finally:
    time.sleep(5)
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (ensure chromedriver is in your PATH or specify the path)
driver = webdriver.Chrome()

try:
    # Navigate to the registration page
    driver.get("https://dashboard.melaka.app/register")

    # Maximize the browser window (optional)
    driver.maximize_window()

    # Wait for the page to load fully
    wait = WebDriverWait(driver, 30)  # Increase wait time if needed
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Find and fill out the registration form fields
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email_field = driver.find_element(By.NAME, "email")
    password_field = driver.find_element(By.NAME, "password")
    nomortelfon_field = driver.find_element(By.NAME, "nomor telefon")
    confirm_password_field = driver.find_element(By.NAME, "confirm_password")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_field.send_keys("your_username")
    email_field.send_keys("your_email@example.com")
    nomortelfon_field("your_email@example.com")
    password_field.send_keys("your_password")
    confirm_password_field.send_keys("your_password")

    # Submit the form
    submit_button.click()

    # Wait for registration to complete (optional)
    # Add more logic here as needed

    # Example: Wait for a success message
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))
    print("Registration Successful!")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the browser
    driver.quit()

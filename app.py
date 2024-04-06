from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize the Firefox WebDriver

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
driver = webdriver.Firefox(options=options)

try:
    # Navigate to the website
    driver.get("https://shouryade.github.io/GA-Pipeline-Workshop/")
    # Find the h1 element
    h1_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(., 'Magic Website')]"))
    )
    print("Test Passed: Found h1 tag containing 'Magic Website'")

except Exception as e:
    print("Test Failed:", e)
finally:
    driver.quit()

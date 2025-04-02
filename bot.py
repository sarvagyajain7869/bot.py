from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# Print environment variables for debugging
print("CHROME_BIN:", os.getenv("CHROME_BIN"))
print("CHROMEDRIVER_PATH:", os.getenv("CHROMEDRIVER_PATH"))

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = os.getenv("CHROME_BIN")
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set Chrome service with the correct executable path
chrome_service = Service(os.getenv("CHROMEDRIVER_PATH"))

# Initialize WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Open a test website
driver.get("https://xvideosfree.unaux.com")
print("Page Title:", driver.title)

# Close the driver
driver.quit()

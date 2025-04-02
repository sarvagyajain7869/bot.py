from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# Print environment variable values for debugging
print("CHROME_BIN:", os.getenv("CHROME_BIN"))
print("CHROMEDRIVER_PATH:", os.getenv("CHROMEDRIVER_PATH"))

# Set Chrome options
chrome_options = Options()
chrome_options.binary_location = os.getenv("CHROME_BIN")
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(executable_path=os.getenv("CHROMEDRIVER_PATH"), options=chrome_options)

# Open a website to test
driver.get("https://xvideosfree.unaux.com")
print("Page Title:", driver.title)

# Close the driver
driver.quit()

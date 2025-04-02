import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Load paths from Railway environment variables
chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/google-chrome")
chromedriver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")

chrome_options = Options()
chrome_options.binary_location = chrome_bin
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set ChromeDriver service
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open your site
URL = "https://code11u.blogspot.com"
driver.get(URL)
print("Website opened successfully!")

driver.quit()

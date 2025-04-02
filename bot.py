from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://code11u.blogspot.com")  # Change this to your Blogger site

time.sleep(random.uniform(2, 5))  # Human-like delay

try:
    buttons = driver.find_elements(By.TAG_NAME, "button")  # Find buttons on page
    if buttons:
        random.choice(buttons).click()
        print("Clicked a button!")
except Exception as e:
    print("Error clicking button:", e)

time.sleep(random.uniform(3, 7))  # Another random delay

# Scroll randomly to simulate human behavior
for _ in range(3):
    driver.execute_script("window.scrollBy(0, 200)")  # Scroll down
    time.sleep(random.uniform(1, 3))

driver.quit()
print("Task Completed!")

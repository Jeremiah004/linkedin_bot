from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize ChromeDriver
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# Add options here if needed, e.g., options.add_argument('--headless')
driver = webdriver.Chrome(service=service, options=options)

# Example usage
driver.get("http://www.example.com")
print(driver.title)
driver.quit()

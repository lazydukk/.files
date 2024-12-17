from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://example.com")

# Find the link to the PDF file
link = driver.find_element(By.LINK_TEXT, "Download PDF")

# Click the link
link.click()

# Wait for the PDF to download
driver.implicitly_wait(10)

# Close the browser
driver.quit()
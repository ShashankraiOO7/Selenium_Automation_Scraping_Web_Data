from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Chrome options
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ssl-version-min=tls1.2')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")


# Initialize driver
s = Service('C:/Users/Shashank Rai/OneDrive/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

# Open IRCTC login page
driver.get('https://www.irctc.co.in/nget/train-search')
time.sleep(5)
menu=driver.find_element(By.XPATH,value="/html/body/app-root/app-home/div[1]/app-header/div[1]/div[2]")
menu.click()
time.sleep(2)
# Click on login button
login_button = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[1]/app-header/div[3]/p-sidebar/div/nav/div/label")
login_button.click()
time.sleep(1)

# Enter username
username_input = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/input")
username_input.send_keys("Raishashnk")  # Replace with your IRCTC username
time.sleep(2)
# Enter password
password_input = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[3]/input")
password_input.send_keys("Srk275305@")  # Replace with your IRCTC password
time.sleep(5)

captcha_element = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[5]/div/app-captcha/div/div/div[2]/span[1]/img")
# Take a screenshot of the CAPTCHA and save it
captcha_element.screenshot("captcha.png")
# Load the saved image with OpenCV
image = cv2.imread("captcha.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Save the processed image (optional for debugging)
cv2.imwrite("processed_captcha.png", thresh)

# Extract the CAPTCHA text using Tesseract
captcha_text = pytesseract.image_to_string(thresh, config='--psm 6').strip()
print(f"Extracted CAPTCHA: {captcha_text}")

captcha_input = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/div[5]/div/app-captcha/div/div/input")
captcha_input.send_keys(captcha_text)

# Click login
submit_button = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/app-login/p-dialog[1]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/form/span/button")
submit_button.click()
time.sleep(1)

# After login, fill in train search details
input0 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input")
input0.send_keys('MAU JN - MAU')
#time.sleep(1)
input0.send_keys(Keys.TAB)

input1 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input")
input1.send_keys('ANAND VIHAR TRM - ANVT')
time.sleep(0.5)
input1.send_keys(Keys.TAB)

#input3 = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
date_input = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")

date_input.click()
date_input.send_keys(Keys.CONTROL + "a")  # Select all text
date_input.send_keys(Keys.DELETE)         # Clear the input
date_input.send_keys("20/03/2025")


dropdown = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[3]/div/div/p-dropdown/div")
dropdown.click()
#time.sleep(1)
tatkal=driver.find_element(By.XPATH,value='/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[3]/div/div/p-dropdown/div/div[4]/div/ul/p-dropdownitem[6]/li/span')
tatkal.click()
Search = driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div[1]")
Search.click()

import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ASUS/Desktop/Server/sheetsCredentials.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet (replace with your sheet name and cell reference)
sheet = client.open("Flutter GSheets").sheet1
cell_value = sheet.cell(1, 1).value  # Replace with your cell reference

# Set up the WebDriver (update the path to match where you've stored chromedriver or geckodriver)
driver = webdriver.Chrome()  # or webdriver.Firefox()
driver.get("https://web.whatsapp.com")

# Wait for QR code scan (user has to scan it manually)
print("Please scan the QR code to log in to WhatsApp Web and press Enter")
input()
print("OK")

try:
    while True:
        current_row_count = sheet.row_count
        print("New message")
        recipient = "963932722234"
        message = sheet.cell(current_row_count, 2).value  # Replace with column number

        # Search for the recipient
        search_box = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']"))
        )
        search_box.clear()  # Clear any previous input
        search_box.click()
        search_box.send_keys(recipient)
        search_box.send_keys(Keys.RETURN)

        # Wait for the chat to load and send the message
        message_box = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']"))
        )
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        print(f"Sent message to {recipient}: {message}")

        # Wait before checking for new messages
        time.sleep(30)

except KeyboardInterrupt:
    print("Exiting the script.")
    driver.quit()

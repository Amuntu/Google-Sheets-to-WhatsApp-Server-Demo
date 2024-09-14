# Google Sheets to WhatsApp Server (without WhatsApp API)
A Python-based demo for automating WhatsApp message sending using data from Google Sheets. Includes scripts for browser automation with Chrome WebDriver.
## install:
### 1) first you need to install the following libraries:
   ```bash
   pip install selenium
   pip install openpyxl
   pip install pandas
   pip install webdriver-manager
   pip install gspread
   pip install oauth2client
   ```
### 2) Get Google sheets Credentials:

To get Google Sheets credentials for integrating with Python, you'll need to follow a few steps:

a) Create a Google Cloud Project: Go to the [Google Cloud Console](https://cloud.google.com/) and create a new project.

b) Enable the Google Sheets API: Within the project, go to the "APIs & Services" section and enable the Google Sheets API and Google Drive API. This allows your project to interact with Google Sheets.

c) Create a Service Account: In the "APIs & Services" section, create a service account. This account will act on your behalf when accessing the Google Sheets data. Generate a key in JSON format during this step and download it.

d) Share Google Sheets with the Service Account: Open your Google Sheet, click the Share button, and add the service account email (found in the JSON file) with Editor access.

## Run:
In order to run project you need to run these two files sepratly:
* `chromedriver.exe`
* `whatsapp_automation.py`

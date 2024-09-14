import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('/path/to/your/sheetCredentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Flutter GSheets").sheet1 #"Flutter GSheets" : Replace it with your our Spreed-Sheet Name.

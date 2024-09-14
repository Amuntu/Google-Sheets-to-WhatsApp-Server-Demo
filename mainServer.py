import gspread
from oauth2client.service_account import ServiceAccountCredentials
# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ASUS/Downloads/cre.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Flutter GSheets").sheet1
print(dir(sheet))

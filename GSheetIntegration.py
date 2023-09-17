import gspread
from google.oauth2 import service_account
# from oauth2client.service_account import ServiceAccountCredentials

# path to json file
jsonKeyFile = 'path to json file'

# create credentials from the JSON key file and add scopes
creds = service_account.Credentials.from_service_account_file(
    jsonKeyFile, scopes=['https://www.googleapis.com/auth/spreadsheets',]
)
# store credentials in a variable 
client = gspread.authorize(creds)

# open google sheets
sheet = client.open('Lead Data').sheet1

# append data to google shoots
with open('leads.csv', 'r') as file:
    csv_data = file.read()
    client.import_csv(sheet.id, csv_data.encode())


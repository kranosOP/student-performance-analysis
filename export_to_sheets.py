import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Authenticate Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("Student Performance Report").sheet1

# Read Data
df = pd.read_csv("performance_data.csv")  # Assuming data is stored in CSV

# Upload data to Google Sheets
sheet.insert_rows(df.values.tolist(), 2)

print("Data successfully uploaded to Google Sheets.")

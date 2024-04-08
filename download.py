import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests


# Step 1: Read URLs from the Spreadsheet
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("bpt-files-71f8d02803dc.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1c1Z2Vpj-fMOSkluhU3-oKS3z16NwDfUc9JoWs4fvDsU").sheet1
urls = sheet.col_values(17)[1:]  # Assuming URLs are in the first column

# Step 2: Download the Files

print(urls)
for url in urls:
    r = requests.get(url, allow_redirects=True)
    filename = "./downloads/" + url.split('/')[-1]
    with open(filename, 'wb') as f:
        f.write(r.content)
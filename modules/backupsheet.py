import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#your API Key
credentials = ServiceAccountCredentials.from_json_keyfile_name('', scope)

#your sheets id
docid = ""

client = gspread.authorize(credentials)
spreadsheet = client.open_by_key(docid)
for i, worksheet in enumerate(spreadsheet.worksheets()):
    filename = docid + '-worksheet' + str(i) + '.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(worksheet.get_all_values())
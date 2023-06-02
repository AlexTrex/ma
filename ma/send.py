from random import randrange
import json

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_service_sacc():
    
    creds_json = "sakeys.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


sheet = get_service_sacc().spreadsheets()

# https://docs.google.com/spreadsheets/d/xxx/edit#gid=0
sheet_id = "175TcJJ-jwFz7cpm69y-ZEOXCSCgmE4wPDdnQClmbwK0"


# https://developers.google.com/resources/api-libraries/documentation/sheets/v4/python/latest/sheets_v4.spreadsheets.html

def get_values():
    values = [[randrange(10, 99),randrange(10, 99)],["Green","Apple"]]
    # values = [[randrange(10, 99) for _ in range(0, 6)]]
    # values = [[randrange(10, 99)] for _ in range(0, 3)]
    # values = [[randrange(10, 99) for _ in range(0, 3)] for _ in range(0, 3)]
    return values

data = None
with open('my.json', encoding="utf-8") as file:
  data = json.load(file)
# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update
resp = sheet.values().update(
    spreadsheetId=sheet_id,
    range="List1",
    valueInputOption="RAW",
    body={'values' : data }).execute()


# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append
# resp = sheet.values().append(
#     spreadsheetId=sheet_id,
#     range="Лист2!A1",
#     valueInputOption="RAW",
#     # insertDataOption="INSERT_ROWS",
#     body={'values' : get_values() }).execute()

# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate
# body = {
#     'valueInputOption' : 'RAW',
#     'data' : [
#         {'range' : 'Лист2!D2', 'values' : get_values()},
#         {'range' : 'Лист2!H4', 'values' : get_values()}
#     ]
# }

# resp = sheet.values().batchUpdate(spreadsheetId=sheet_id, body=body).execute()


print(resp)

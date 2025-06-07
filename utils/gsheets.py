import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def connect_sheet(sheet_name='SalonBookings'):
    scope = ['https://spreadsheets.google.com/feeds', 
             'https://www.googleapis.com/auth/drive'] 

    credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
    gc = gspread.authorize(credentials)
    sh = gc.open(sheet_name)
    return sh

def get_bookings_df():
    sh = connect_sheet()
    worksheet = sh.worksheet("Bookings")
    df = pd.DataFrame(worksheet.get_all_records())
    return df

def save_booking(data):
    sh = connect_sheet()
    worksheet = sh.worksheet("Bookings")
    worksheet.append_row(list(data.values()))

def get_promos_df():
    sh = connect_sheet()
    worksheet = sh.worksheet("Promos")
    df = pd.DataFrame(worksheet.get_all_records())
    return df
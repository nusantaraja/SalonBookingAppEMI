import gspread
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

# Nama spreadsheet Anda di Google Sheets
sheet_name = "Nama_Spreadsheet_Anda_Disini" # <-- GANTI DENGAN NAMA SPREADSHEET ANDA

def connect_sheet():
    """Menghubungkan ke Google Sheet menggunakan kredensial dari st.secrets."""
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    # Mengambil kredensial dari Streamlit Secrets
    # Streamlit secara otomatis membaca dari "gcp_service_account" jika formatnya benar.
    creds_json = st.secrets["gcp_service_account"]
    
    # Menggunakan from_json_keyfile_dict karena kita punya dictionary, bukan nama file
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    
    gc = gspread.authorize(credentials)
    sh = gc.open(sheet_name)
    return sh

def append_booking_data(data):
    """Menambahkan data booking baru ke worksheet 'Bookings'."""
    sh = connect_sheet()
    worksheet = sh.worksheet("Bookings") # Pastikan nama worksheet ini benar
    worksheet.append_row(list(data.values()))

def get_promos_df():
    """Mengambil data promo dari worksheet 'Promos' dan mengembalikannya sebagai DataFrame."""
    sh = connect_sheet()
    worksheet = sh.worksheet("Promos") # Pastikan nama worksheet ini benar
    df = pd.DataFrame(worksheet.get_all_records())
    return df

def get_all_bookings_df():
    """Mengambil semua data booking dari worksheet 'Bookings'."""
    sh = connect_sheet()
    worksheet = sh.worksheet("Bookings")
    df = pd.DataFrame(worksheet.get_all_records())
    return df
    
# --- END OF FILE utils/gsheets.py (FIXED & SECURE) ---
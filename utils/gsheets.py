# --- START OF FILE utils/gsheets.py (UPDATED WITH YOUR INFO) ---

import gspread
import pandas as pd
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

# Nama spreadsheet Anda di Google Sheets
# INI SUDAH DISESUAIKAN DENGAN INFORMASI ANDA
sheet_name = "SalonJennifer"

def connect_sheet():
    """Menghubungkan ke Google Sheet menggunakan kredensial dari st.secrets."""
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    # Mengambil kredensial dari Streamlit Secrets
    creds_json = st.secrets["gcp_service_account"]
    
    # Menggunakan from_json_keyfile_dict karena kita punya dictionary, bukan nama file
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    
    gc = gspread.authorize(credentials)
    sh = gc.open(sheet_name) # Akan membuka spreadsheet bernama "SalonJennifer"
    return sh

def append_booking_data(data):
    """Menambahkan data booking baru ke worksheet 'Bookings'."""
    try:
        sh = connect_sheet()
        worksheet = sh.worksheet("Bookings") # Pastikan worksheet 'Bookings' ada di file "SalonJennifer"
        worksheet.append_row(list(data.values()))
        return True
    except gspread.exceptions.WorksheetNotFound:
        st.error("Worksheet 'Bookings' tidak ditemukan di dalam Google Sheet.")
        return False
    except Exception as e:
        st.error(f"Terjadi kesalahan saat menyimpan data: {e}")
        return False

def get_promos_df():
    """Mengambil data promo dari worksheet 'Promos' dan mengembalikannya sebagai DataFrame."""
    try:
        sh = connect_sheet()
        worksheet = sh.worksheet("Promos") # Pastikan worksheet 'Promos' ada di file "SalonJennifer"
        df = pd.DataFrame(worksheet.get_all_records())
        return df
    except gspread.exceptions.WorksheetNotFound:
        st.error("Worksheet 'Promos' tidak ditemukan. Pastikan ada tab bernama 'Promos' di Google Sheet Anda.")
        return pd.DataFrame() # Kembalikan DataFrame kosong agar aplikasi tidak crash
    except Exception as e:
        st.error(f"Gagal mengambil data promo: {e}")
        return pd.DataFrame()

def get_all_bookings_df():
    """Mengambil semua data booking dari worksheet 'Bookings'."""
    try:
        sh = connect_sheet()
        worksheet = sh.worksheet("Bookings")
        df = pd.DataFrame(worksheet.get_all_records())
        return df
    except gspread.exceptions.WorksheetNotFound:
        st.error("Worksheet 'Bookings' tidak ditemukan. Pastikan ada tab bernama 'Bookings' di Google Sheet Anda.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Gagal mengambil data booking: {e}")
        return pd.DataFrame()

def add_promo(data):
    """Menambahkan data promo baru ke worksheet 'Promos'."""
    try:
        sh = connect_sheet()
        worksheet = sh.worksheet("Promos")
        worksheet.append_row(list(data.values()))
        return True
    except Exception as e:
        st.error(f"Gagal menambahkan promo: {e}")
        return False

# --- END OF FILE utils/gsheets.py (UPDATED WITH YOUR INFO) ---
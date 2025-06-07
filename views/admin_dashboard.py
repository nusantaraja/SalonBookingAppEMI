# --- START OF FILE pages/admin_dashboard.py (FIXED) ---

import streamlit as st
from utils import gsheets
import pandas as pd

def show():
    st.title("🔐 Dashboard Admin Salon")
    st.markdown("---")

    st.subheader("Daftar Semua Booking Pelanggan")

    # Ambil data booking
    # Menggunakan nama fungsi yang benar: get_all_bookings_df
    bookings_df = gsheets.get_all_bookings_df()

    if not bookings_df.empty:
        # Tampilkan data dengan urutan terbaru di atas
        st.dataframe(bookings_df.sort_values(by="Timestamp", ascending=False), use_container_width=True)
    else:
        st.info("Belum ada data booking yang masuk.")

    st.markdown("---")
    st.subheader("Daftar Promo Aktif")
    
    # Ambil data promo
    promos_df = gsheets.get_promos_df()
    
    if not promos_df.empty:
        st.dataframe(promos_df, use_container_width=True)
    else:
        st.info("Belum ada data promo yang terdaftar.")

# --- END OF FILE pages/admin_dashboard.py (FIXED) ---
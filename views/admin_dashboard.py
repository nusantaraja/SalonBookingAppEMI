# --- START OF FILE pages/admin_dashboard.py (UPGRADED) ---

import streamlit as st
from utils import gsheets
import pandas as pd

def show():
    st.title("🔐 Dashboard Admin Salon")
    st.markdown("---")

    # --- BAGIAN MANAJEMEN PROMO ---
    st.subheader("Manajemen Promo")
    with st.form("promo_form", clear_on_submit=True):
        st.write("Tambahkan Kode Promo Baru:")
        col1, col2 = st.columns(2)
        with col1:
            new_promo_code = st.text_input("Kode Promo Baru", placeholder="Contoh: RAMBUTBARU")
        with col2:
            new_promo_discount = st.number_input("Diskon (%)", min_value=1, max_value=100, step=1)
        
        submitted_promo = st.form_submit_button("Tambahkan Promo")

        if submitted_promo:
            if new_promo_code:
                data_promo = {
                    "Kode": new_promo_code,
                    "Diskon (%)": new_promo_discount
                }
                success = gsheets.add_promo(data_promo)
                if success:
                    st.success(f"Promo '{new_promo_code}' berhasil ditambahkan!")
                else:
                    st.error("Gagal menambahkan promo.")
            else:
                st.warning("Kode promo tidak boleh kosong.")

    # --- BAGIAN MELIHAT PROMO & BOOKING ---
    tab1, tab2 = st.tabs(["📊 Daftar Semua Booking", "🎟️ Daftar Promo Aktif"])

    with tab1:
        st.subheader("Daftar Semua Booking Pelanggan")
        bookings_df = gsheets.get_all_bookings_df()
        if not bookings_df.empty:
            st.dataframe(bookings_df.sort_values(by="Timestamp", ascending=False), use_container_width=True)
        else:
            st.info("Belum ada data booking yang masuk.")

    with tab2:
        st.subheader("Daftar Promo Aktif")
        promos_df = gsheets.get_promos_df()
        if not promos_df.empty:
            st.dataframe(promos_df, use_container_width=True)
        else:
            st.info("Belum ada data promo yang terdaftar.")

# --- END OF FILE pages/admin_dashboard.py (UPGRADED) ---
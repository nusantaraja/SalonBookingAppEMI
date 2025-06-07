# --- START OF FILE pages/customer_booking.py (UPGRADED) ---

import streamlit as st
from utils import gsheets
from datetime import datetime
import pandas as pd

# DAFTAR HARGA LAYANAN (Bisa Anda sesuaikan)
HARGA_LAYANAN = {
    "Potong Rambut (Pria)": 50000,
    "Potong Rambut (Wanita)": 75000,
    "Creambath": 100000,
    "Manicure & Pedicure": 120000,
    "Facial": 150000,
    "Lainnya": 0  # Harga 0 untuk 'Lainnya', bisa dikonfirmasi manual
}

def show():
    st.title("📝 Formulir Booking Pelanggan")

    # Ambil data promo
    promos_df = gsheets.get_promos_df()
    if promos_df.empty or 'Kode' not in promos_df.columns:
        promos_df = pd.DataFrame(columns=['Kode', 'Diskon (%)'])

    with st.form("booking_form", clear_on_submit=True):
        st.subheader("Data Diri Pelanggan")
        nama_lengkap = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")

        st.subheader("Detail Layanan & Jadwal")
        layanan = st.selectbox("Pilih Layanan", list(HARGA_LAYANAN.keys()))
        
        # Tampilkan harga awal secara dinamis
        harga_awal = HARGA_LAYANAN.get(layanan, 0)
        st.info(f"Harga Awal: Rp {harga_awal:,.0f}".replace(",", "."))

        tanggal_booking = st.date_input("Tanggal Booking")
        waktu_booking = st.time_input("Waktu Booking")

        st.subheader("Promo")
        promo_code = st.text_input("Masukkan Kode Promo (opsional)")

        submitted = st.form_submit_button("Booking Sekarang")

        if submitted:
            if not nama_lengkap:
                st.warning("Nama Lengkap wajib diisi.")
            else:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                diskon = 0
                pesan_promo = ""

                # Hitung diskon jika kode promo valid
                if promo_code and not promos_df.empty:
                    if promo_code in promos_df['Kode'].values:
                        diskon = promos_df[promos_df['Kode'] == promo_code]['Diskon (%)'].iloc[0]
                        pesan_promo = f"Selamat! Anda mendapatkan diskon {diskon}%."
                    else:
                        pesan_promo = "Kode promo tidak valid."
                        promo_code = "" # Kosongkan jika tidak valid

                harga_final = harga_awal * (1 - (diskon / 100))

                # Siapkan data untuk disimpan
                data_to_save = {
                    "Timestamp": timestamp,
                    "Nama Lengkap": nama_lengkap,
                    "Pilih Layanan": layanan,
                    "Tanggal Booking": str(tanggal_booking),
                    "Waktu Booking": str(waktu_booking),
                    "Kode Promo": promo_code,
                    "Harga Awal": harga_awal,
                    "Harga Final (Setelah Diskon)": harga_final
                }

                success = gsheets.append_booking_data(data_to_save)

                if success:
                    st.success("Booking Anda telah berhasil disimpan! Terima kasih.")
                    if pesan_promo:
                        st.info(pesan_promo)
                    st.balloons()
                    st.markdown(f"### Total Bayar: **Rp {harga_final:,.0f}**".replace(",", "."))
                else:
                    st.error("Gagal menyimpan booking. Silakan coba lagi.")

# --- END OF FILE pages/customer_booking.py (UPGRADED) ---
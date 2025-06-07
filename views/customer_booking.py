# --- START OF FILE pages/customer_booking.py (FIXED & ADJUSTED) ---

import streamlit as st
from utils import gsheets
from datetime import datetime
import pandas as pd

def show():
    st.title("📝 Formulir Booking Pelanggan")

    # Ambil data promo terlebih dahulu untuk memeriksa kode
    try:
        promos_df = gsheets.get_promos_df()
        if promos_df.empty and 'Kode' not in promos_df.columns:
            # Jika dataframe kosong atau tidak ada kolom 'Kode', buat kolom dummy
            # agar aplikasi tidak error saat memeriksa promo
            promos_df = pd.DataFrame(columns=['Kode', 'Diskon (%)'])
    except Exception as e:
        st.warning(f"Tidak dapat memuat data promo. Fitur kode promo mungkin tidak berfungsi. Error: {e}")
        promos_df = pd.DataFrame(columns=['Kode', 'Diskon (%)'])

    with st.form("booking_form", clear_on_submit=True):
        st.subheader("Data Diri Pelanggan")
        nama_lengkap = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")

        st.subheader("Detail Layanan & Jadwal")
        layanan = st.selectbox(
            "Pilih Layanan",
            [
                "Potong Rambut (Pria)",
                "Potong Rambut (Wanita)",
                "Creambath",
                "Manicure & Pedicure",
                "Facial",
                "Lainnya"
            ]
        )
        tanggal_booking = st.date_input("Tanggal Booking")
        waktu_booking = st.time_input("Waktu Booking")

        st.subheader("Promo")
        promo_code = st.text_input("Masukkan Kode Promo (opsional)", placeholder="Contoh: DISKONBARU")

        # Tombol submit form
        submitted = st.form_submit_button("Booking Sekarang")

        if submitted:
            # Validasi input sederhana
            if not nama_lengkap:
                st.warning("Nama Lengkap wajib diisi.")
            else:
                # Siapkan data sesuai urutan kolom di Google Sheet
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Cek validitas kode promo
                if promo_code and not promos_df.empty:
                    if promo_code in promos_df['Kode'].values:
                        st.info(f"Kode promo '{promo_code}' berhasil digunakan!")
                    else:
                        st.warning(f"Kode promo '{promo_code}' tidak valid, booking tetap dilanjutkan tanpa promo.")
                        promo_code = "" # Kosongkan kode promo jika tidak valid
                elif promo_code:
                     st.warning(f"Kode promo '{promo_code}' tidak dapat divalidasi, booking tetap dilanjutkan tanpa promo.")
                     promo_code = "" # Kosongkan kode promo jika tidak valid

                # Urutan data harus PERSIS SAMA dengan kolom di Google Sheet
                data_to_save = {
                    "Timestamp": timestamp,
                    "Nama Lengkap": nama_lengkap,
                    "Pilih Layanan": layanan,
                    "Tanggal Booking": str(tanggal_booking), # Ubah ke string
                    "Waktu Booking": str(waktu_booking),     # Ubah ke string
                    "Kode Promo": promo_code
                }

                # Panggil fungsi untuk menyimpan ke Google Sheet
                success = gsheets.append_booking_data(data_to_save)

                if success:
                    st.success("Booking Anda telah berhasil disimpan! Terima kasih.")
                else:
                    st.error("Gagal menyimpan booking. Silakan coba lagi.")

    st.markdown("---")
    st.info("Setelah melakukan booking, Anda akan dihubungi oleh admin kami untuk konfirmasi lebih lanjut.")

# --- END OF FILE pages/customer_booking.py (FIXED & ADJUSTED) ---
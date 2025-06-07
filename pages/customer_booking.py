import streamlit as st
from utils import gsheets

def show():
    st.title("📅 Booking Layanan Salon")

    name = st.text_input("Nama Lengkap")
    service = st.selectbox("Pilih Layanan", [
        "Potong Rambut",
        "Creambath",
        "Manicure",
        "Makeup",
        "Facial"
    ])
    date = st.date_input("Tanggal Booking")
    time = st.time_input("Waktu Booking")

    promo_code = st.text_input("Masukkan Kode Promo (opsional)")
    promos = gsheets.get_promos_df()
    discount = 0
    if promo_code in promos['Kode'].values:
        discount = promos[promos['Kode'] == promo_code]['Diskon (%)'].values[0]
        st.success(f"Promo {promo_code} berhasil diterapkan! Diskon {discount}%")

    if st.button("Pesan Sekarang"):
        bookings = gsheets.get_bookings_df()
        conflict = bookings[(bookings['Tanggal'] == str(date)) & (bookings['Waktu'] == time.strftime("%H:%M"))]

        if not conflict.empty:
            st.error("Maaf, waktu ini sudah dibooking.")
        else:
            data = {
                "Nama": name,
                "Layanan": service,
                "Tanggal": str(date),
                "Waktu": time.strftime("%H:%M"),
                "Status": "Pending"
            }
            gsheets.save_booking(data)
            st.success("Terima kasih! Booking Anda telah berhasil.")

    st.subheader("Riwayat Booking Anda")
    bookings = gsheets.get_bookings_df()
    user_bookings = bookings[bookings['Nama'] == name]
    if not user_bookings.empty:
        st.dataframe(user_bookings[['Layanan', 'Tanggal', 'Waktu', 'Status']])
    else:
        st.info("Anda belum melakukan booking apapun.")
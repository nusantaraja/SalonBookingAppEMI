import streamlit as st
from utils import gsheets

def show():
    st.title("🔐 Dashboard Admin Salon")

    st.subheader("Daftar Semua Booking")
    bookings = gsheets.get_bookings_df()
    st.dataframe(bookings)

    st.subheader("Daftar Promo")
    promos = gsheets.get_promos_df()
    st.dataframe(promos)
# --- START OF FILE salon_app.py (FINAL & CLEAN) ---

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
# Import dari folder 'views' yang baru
from views import customer_booking, admin_dashboard

# --- Konfigurasi Halaman & Autentikasi ---
st.set_page_config(page_title="Salon Jennifer", layout="centered")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- Navigasi Utama di Sidebar ---
st.sidebar.title("💇‍♀️ Salon Jennifer")
page = st.sidebar.radio(
    "Pilih Halaman:",
    ("Booking Pelanggan", "Login Admin")
)

# --- Logika Tampilan Halaman ---

# 1. Halaman Booking Pelanggan (Publik, tidak perlu login)
if page == "Booking Pelanggan":
    customer_booking.show()

# 2. Halaman Login Admin
elif page == "Login Admin":
    st.title("🔒 Halaman Login Admin")
    
    authenticator.login()

    if st.session_state["authentication_status"]:
        st.sidebar.success(f"Login sebagai *{st.session_state['name']}*")
        admin_dashboard.show()
        
        with st.sidebar:
            st.markdown("---")
            authenticator.logout()

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password yang Anda masukkan salah.')
        st.warning('Lupa password? Hubungi pemilik salon.')

    elif st.session_state["authentication_status"] is None:
        st.info('Silakan masukkan username dan password admin untuk melihat dashboard.')

# --- END OF FILE salon_app.py (FINAL & CLEAN) ---
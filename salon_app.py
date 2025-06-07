# --- START OF FILE salon_app.py (FIXED) ---

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Salon Rambut & Kecantikan", layout="centered")

# --- AUTHENTICATION ---
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Panggil method login(). Ini akan merender form login
# dan menangani pembaruan session_state secara internal.
authenticator.login()

# --- MAIN APP LOGIC ---

if st.session_state["authentication_status"]:
    # Jika login berhasil, tampilkan konten utama aplikasi dan tombol logout di sidebar.
    
    # Menampilkan tombol logout dan nama user di sidebar
    with st.sidebar:
        st.title(f"Selamat datang, *{st.session_state['name']}*")
        authenticator.logout() # Tombol logout dengan sintaks baru

    st.sidebar.title("Navigasi")
    page = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Booking Pelanggan", "Dashboard Admin"])

    if page == "Beranda":
        st.title("💇‍♀️ Salon Rambut & Kecantikan")
        st.markdown("Aplikasi ini membantu Anda untuk melakukan booking layanan kecantikan secara online.")
        st.success("Anda berhasil login!")

    elif page == "Booking Pelanggan":
        # Pastikan file pages/customer_booking.py ada
        from pages import customer_booking
        customer_booking.show()

    elif page == "Dashboard Admin":
        # Pastikan file pages/admin_dashboard.py ada
        from pages import admin_dashboard
        admin_dashboard.show()

elif st.session_state["authentication_status"] is False:
    # Jika login gagal
    st.error('Username/password yang Anda masukkan salah')

elif st.session_state["authentication_status"] is None:
    # Jika belum ada input login
    st.warning('Silakan masukkan username dan password Anda')

# --- END OF FILE salon_app.py (FIXED) ---
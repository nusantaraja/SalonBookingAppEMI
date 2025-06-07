import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Salon Rambut & Kecantikan", layout="centered")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

st.sidebar.title("Navigasi")
authenticator.login('Login', 'sidebar')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.write(f"Selamat datang *{st.session_state['name']}*")

    page = st.sidebar.selectbox("Pilih Halaman", ["Beranda", "Booking Pelanggan", "Dashboard Admin"])

    if page == "Beranda":
        st.title("💇‍♀️ Salon Rambut & Kecantikan")
        st.markdown("Aplikasi ini membantu Anda untuk melakukan booking layanan kecantikan secara online.")

    elif page == "Booking Pelanggan":
        from pages import customer_booking
        customer_booking.show()

    elif page == "Dashboard Admin":
        from pages import admin_dashboard
        admin_dashboard.show()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password salah')
elif st.session_state["authentication_status"] is None:
    st.warning('Silakan masukkan username dan password')
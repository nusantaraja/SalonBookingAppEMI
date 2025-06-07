# --- START OF FILE generate_hash.py (CORRECTED LOGIC) ---

import streamlit_authenticator as stauth
import yaml

# 🔐 Password tunggal yang ingin di-hash (sebagai string, bukan list)
password_to_hash = "admin123"

# 🔐 Generate hashed password menggunakan method .hash()
# Method .hash() menerima satu string, bukan list.
hashed_password = stauth.Hasher().hash(password_to_hash)

# Cetak hash ke terminal untuk verifikasi
print(f"Generated Hash: {hashed_password}")

# 📁 Buat konfigurasi YAML untuk config.yaml
config_data = {
    "cookie": {
        "name": "salon_app_cookie",
        "key": "a_very_secret_key_12345", # Ganti dengan kunci rahasia unik Anda
        "expiry_days": 30
    },
    "preauthorized": {
        "emails": []
    },
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Super Admin Salon",
                "email": "admin@example.com",
                "password": hashed_password  # Masukkan hash yang sudah dibuat
            }
        }
    }
}

# 📄 Simpan ke file config.yaml
config_filename = "config.yaml"
with open(config_filename, "w") as file:
    yaml.dump(config_data, file, default_flow_style=False)

print(f"\n✅ Password untuk 'admin' telah di-hash dan disimpan di {config_filename}")
print(f"🔓 Username: admin")
print(f"🔓 Password Plaintext: {password_to_hash} (gunakan ini untuk login di aplikasi)")

# --- END OF FILE generate_hash.py (CORRECTED LOGIC) ---
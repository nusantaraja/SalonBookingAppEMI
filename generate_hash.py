# --- START OF FILE generate_hash.py (FIXED) ---

import streamlit_authenticator as stauth
import yaml
from pathlib import Path

# 🔐 Password default
passwords_to_hash = ["admin123"]

# 🔐 Generate hashed passwords
# Sintaks baru: Buat objek Hasher() dulu, lalu panggil .generate() dengan list password
hashed_passwords = stauth.Hasher().generate(passwords_to_hash)

# Karena kita hanya hash satu password, kita ambil yang pertama dari list
hashed_password = hashed_passwords[0]

# Cetak hash ke terminal (berguna untuk debugging)
print(f"Generated Hash: {hashed_password}")

# 📁 Buat konfigurasi YAML untuk config.yaml
config_data = {
    "cookie": {
        "name": "salon_app_cookie",
        "key": "some_secret_key_here", # Ganti dengan kunci rahasia Anda sendiri untuk keamanan
        "expiry_days": 1
    },
    "preauthorized": {
        "emails": []
    },
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Super Admin Salon",
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
print(f"🔓 Password Plaintext: {passwords_to_hash[0]} (gunakan ini untuk login di aplikasi)")

# --- END OF FILE generate_hash.py (FIXED) ---
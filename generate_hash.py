import streamlit_authenticator as stauth
import yaml
from pathlib import Path

# 🔐 Password default
password = "admin123"

# 🔐 Generate hashed password
hashed = stauth.Hasher([password]).generate()
hashed_password = hashed[0]
print(hashed[0])

# 📁 Buat konfigurasi YAML untuk config.yaml
config_data = {
    "cookie": {
        "name": "salon_app_cookie",
        "key": "some_secret_key_here",
        "expiry_days": 1
    },
    "preauthorized": {
        "emails": []
    },
    "credentials": {
        "usernames": {
            "admin": {
                "name": "Super Admin Salon",
                "password": hashed_password
            }
        }
    }
}

# 📄 Simpan ke file config.yaml
with open("config.yaml", "w") as file:
    yaml.dump(config_data, file, default_flow_style=False)

print(f"✅ Password untuk 'admin' telah di-hash dan disimpan di config.yaml")
print(f"🔓 Username: admin")
print(f"🔓 Password: {password} (gunakan untuk login)")
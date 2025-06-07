# 💇‍♀️ Aplikasi Booking Salon Rambut & Kecantikan

Aplikasi ini dibuat dengan **Streamlit** untuk memudahkan proses booking layanan di salon secara online. Dilengkapi dengan:

- Login Admin aman
- Sistem booking tanpa bentrok
- Promo/Voucher
- Simpan data ke Google Sheets

---

🗂 Struktur Repo Final

```
SalonBookingAppEMI/
│
├── salon_app.py            # Main app
├── requirements.txt            # Library Python
├── config.yaml                 # Konfigurasi login admin
├── README.md                   # Panduan penggunaan
├── LICENSE                     # MIT License
│
├── utils/
│   └── gsheets.py              # Fungsi akses Google Sheets
│
└── pages/
    ├── customer_booking.py     # Halaman booking pelanggan
    └── admin_dashboard.py      # Dashboard admin
```



---
## ✅ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| Login Admin | Menggunakan `streamlit-authenticator` |
| Booking Pelanggan | Pilih layanan, tanggal, waktu |
| Promo Code | Diskon otomatis jika kode valid |
| Validasi Waktu | Mencegah booking waktu yang sudah dipakai |
| Google Sheets | Sebagai database sederhana |

---

## ⚙️ Setup Awal

### 1. Clone repo

```bash
git clone https://github.com/nusantaraja/SalonBookingAppEMI.git
cd SalonBookingAppEMI
🧠 VARK Expert System
Sistem pakar sederhana berbasis **Streamlit** untuk mengidentifikasi gaya belajar seseorang menggunakan model **VARK** (*Visual, Aural, Read/Write, Kinesthetic*). Aplikasi ini memberikan hasil diagnosis serta rekomendasi metode belajar yang sesuai.

🌐 Live Demo
Aplikasi sudah di-deploy dan dapat diakses langsung tanpa instalasi:
👉 https://vark-expert-system.streamlit.app/

📂 Struktur Project
VARK_EXPERT_SYSTEM/
├── .streamlit/
│   └── config.toml       # Konfigurasi UI (Theme)
├── modules/
│   ├── data.py           # Database pertanyaan & rule
│   ├── logic.py          # Logika inferensi sistem pakar
│   └── ui.py             # Komponen antarmuka (Frontend)
├── app.py                # Main entry point aplikasi
└── requirements.txt      # Daftar dependensi library

💻 Cara Menjalankan di Local (Laptop)
1. Install Library
Pastikan Python sudah terinstall, buka terminal di folder project dan jalankan:
pip install -r requirements.txt

2. Jalankan Aplikasi
Ketik perintah berikut untuk memulai server Streamlit:
streamlit run app.py

3. Akses Aplikasi
Browser akan otomatis terbuka. Jika tidak, akses link berikut secara manual: http://localhost:8501

4. Berhenti (Stop)
Untuk mematikan aplikasi, kembali ke terminal lalu tekan tombol: Ctrl + C

🛠️ Teknologi
Language: Python 3
Framework: Streamlit
Visualization: Altair / Pandas
Logic: Rule-Based System (Forward Chaining)

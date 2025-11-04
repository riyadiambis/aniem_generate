🌸 AI WAIFU Generate

Lihat Aplikasi Live di Sini!

https://waifugenai.streamlit.app/

Ini adalah proyek aplikasi web sederhana yang dibuat untuk "mewujudkan halu menjadi WAIFU". Aplikasi ini memungkinkan pengguna memasukkan deskripsi (prompt), dan AI akan menghasilkan gambar karakter anime (waifu) berdasarkan deskripsi tersebut.

Proyek ini dibuat menggunakan Python dengan framework Streamlit dan menggunakan model AI DALL-E 3 dari OpenAI untuk menghasilkan gambar.

(Ganti URL di atas dengan link ke screenshot aplikasi Anda yang sudah jadi)

💻 Teknologi yang Digunakan

Python: Bahasa pemrograman utama.

Streamlit: Framework untuk membuat antarmuka web (UI) dengan cepat.

OpenAI API: Menggunakan model DALL-E 3 untuk backend penghasil gambar.

Git & GitHub: Untuk version control dan hosting repositori.

Streamlit Community Cloud: Untuk deployment (hosting) aplikasi secara gratis.

🚀 Cara Menjalankan Proyek Ini Secara Lokal

Jika Anda ingin menjalankan proyek ini di komputer Anda sendiri:

1. Clone Repositori

git clone [https://github.com/riyadiambis/aniem_generate.git](https://github.com/riyadiambis/aniem_generate.git)
cd aniem_generate


(Ganti URL di atas dengan URL repositori GitHub Anda yang benar)

2. Buat Virtual Environment (Sangat Direkomendasikan)
Ini agar library Python Anda tidak tercampur.

# Buat environment
python -m venv venv

# Aktifkan (untuk Windows)
.\venv\Scripts\activate


3. Install Semua Kebutuhan
File requirements.txt sudah berisi semua library yang dibutuhkan.

pip install -r requirements.txt


4. Siapkan API Key Anda
Buat file baru di dalam folder proyek Anda dengan nama .env.

.env


Buka file .env tersebut dan isi dengan API key OpenAI Anda (yang sudah Anda beli kreditnya $5):

OPENAI_API_KEY="sk-kunci-rahasia-anda-tempel-di-sini"


5. Jalankan Aplikasi!
Gunakan perintah Streamlit di terminal Anda:

streamlit run anime-generate.py


(Nama file anime-generate.py ini harus sama dengan nama file Python utama Anda, seperti di screenshot Anda).

📁 Struktur File Proyek

/aniem_generate
│
├── .env                  <-- Berisi API Key (RAHASIA, tidak di-push)
├── .gitignore            <-- Memberi tahu Git untuk mengabaikan .env
├── anime-generate.py     <-- Kode utama aplikasi Streamlit
└── requirements.txt      <-- Daftar pustaka yang dibutuhkan (streamlit, openai, etc.)


💡 Pelajaran Penting dari Proyek Ini

Keamanan API Key: Belajar bahwa API Key adalah rahasia dan tidak boleh di-push ke GitHub.

.gitignore: Cara yang benar untuk mengabaikan file .env agar tidak ter-upload.

Streamlit Secrets: Cara yang aman untuk menggunakan API Key saat deployment adalah dengan menyimpannya di "Secrets" di dasbor Streamlit Cloud, bukan di dalam kode.
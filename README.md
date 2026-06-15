# ✈️ Aviation Ground School Bot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Gemini API](https://img.shields.io/badge/Gemini_API-2.5_Flash-orange.svg)](https://ai.google.dev/)

**Aviation Ground School Bot** adalah asisten instruktur virtual berbasis Artificial Intelligence (LLM) yang dirancang khusus untuk membantu *student pilot* dalam mempelajari dan mempersiapkan ujian lisensi PPL (*Private Pilot License*).

Dibangun menggunakan integrasi **Google Gemini API** dan antarmuka **Streamlit**, bot ini berfokus pada penyampaian materi prosedural, evaluasi, dan simulasi penerbangan dasar, khususnya untuk operasional pesawat **Cessna 172**.

---

## ✨ Fitur Utama

Aplikasi ini diinstruksikan melalui *Prompt Engineering* yang ketat untuk menguasai 5 silabus utama *ground school*:

1. **Principles of Flight:** Penjelasan aerodinamika dasar (Lift, Weight, Thrust, Drag).
2. **Aircraft Systems & Instruments:** Anatomi instrumen penerbangan dan sistem kelistrikan/bahan bakar Cessna 172.
3. **Aviation Meteorology:** Panduan membaca cuaca penerbangan (METAR/TAF) dan identifikasi bahaya cuaca.
4. **Navigation & Flight Planning:** Perhitungan rute, penggunaan *dead reckoning*, dan pemahaman instrumen VOR.
5. **Air Law & Regulations:** Regulasi ruang udara standar ICAO/FAA.

*Dilengkapi dengan fitur **Memory (Session State)**, bot ini mampu mengingat konteks percakapan sebelumnya dan memberikan kuis evaluasi pilihan ganda yang interaktif.*

---

## 🚀 Live Demo

Aplikasi ini telah di-deploy ke publik dan dapat diakses secara langsung tanpa proses instalasi melalui tautan berikut:

**[▶ Mainkan Live Demo di Sini](https://aviation-ground-school-bot.streamlit.app/)**

---

## 🛠️ Instalasi & Setup Lokal

Jika Anda ingin menjalankan atau memodifikasi proyek ini secara lokal, ikuti langkah-langkah berikut:

### 1. Clone Repositori

```bash
git clone https://github.com/andriilaksono/aviation-ground-school-bot.git
cd aviation-ground-school-bot
```

### 2. Buat Virtual Environment & Instal Dependensi

```bash
python -m venv env

# Windows:
.\env\Scripts\activate

# Mac/Linux:
source env/bin/activate

pip install -r requirements.txt
```

### 3. Konfigurasi API Key

Dapatkan API Key dari [Google AI Studio](https://aistudio.google.com/). Kemudian buat folder dan file `secrets.toml` di dalam direktori proyek:

```bash
mkdir .streamlit
echo 'GEMINI_API_KEY = "masukkan_api_key_anda_di_sini"' > .streamlit/secrets.toml
```

### 4. Jalankan Aplikasi

```bash
streamlit run app.py
```

---

## 🏗️ Struktur Direktori

```
📦 aviation-ground-school-bot
 ┣ 📜 app.py               # Main application script & LLM integration
 ┣ 📜 requirements.txt     # Python dependencies
 ┣ 📜 .gitignore           # Ignored files (env, secrets, etc.)
 ┗ 📜 README.md            # Project documentation
```

---

## 👨‍💻 Penulis

Dikembangkan oleh **Andri Laksono** sebagai proyek eksplorasi integrasi LLM dan pengembangan asisten AI spesifik domain (*domain-specific AI assistant*).

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Aviation Study Buddy", page_icon="✈️", layout="centered")
st.title("✈️ Aviation Ground School Bot")
st.caption("Asisten AI untuk materi Private Pilot License (PPL) dan operasional Cessna 172.")

# 1. Ambil API Key dari Streamlit Secrets secara aman
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("🚨 API Key belum dikonfigurasi di Streamlit Secrets!")
    st.stop()

# 2. Setup Model & Memory (Session State)
if "chat_session" not in st.session_state:
    st.session_state.chat_session = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.chat_session is None:
    system_prompt = """
    Kamu adalah Instruktur Ground School Penerbangan profesional.
    Tugasmu: Memberikan materi, bimbingan, dan evaluasi kepada student pilot yang sedang mempersiapkan ujian lisensi PPL, dengan fokus pada operasional Cessna 172.

    Silabus yang kamu kuasai:
    1. Principles of Flight (Aerodinamika)
    2. Aircraft Systems & Instruments
    3. Aviation Meteorology
    4. Navigation & Flight Planning
    5. Air Law & Regulations

    Instruksi tambahan:
    - Jika pengguna meminta materi, jelaskan secara terstruktur, akurat, dan gunakan analogi yang mudah dipahami.
    - Selalu tegaskan bahwa jawabanmu adalah untuk tujuan edukasi dan simulasi, bukan pengganti manual operasional pesawat resmi (POH).
    - Berikan format teks yang rapi menggunakan bullet points atau tabel jika menjelaskan spesifikasi pesawat.
    """
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_prompt
    )
    st.session_state.chat_session = model.start_chat(history=[])

# 3. Tampilkan Histori Percakapan di UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Logika Interaksi Chat
if prompt := st.chat_input("Ketik pertanyaan seputar materi ground school di sini..."):
    # Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Kirim ke Gemini dan dapatkan respon
    with st.chat_message("assistant"):
        with st.spinner("Instruktur sedang memikirkan jawaban..."):
            try:
                response = st.session_state.chat_session.send_message(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
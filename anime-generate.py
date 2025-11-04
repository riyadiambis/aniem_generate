import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import io

# 1. Memuat variabel lingkungan dari file .env
load_dotenv()

# 2. Inisialisasi Klien GenAI (Disederhanakan)
try:
    client = OpenAI(
        api_key=os.getenv('OPEN_AI_API')
    )
except Exception as e:
    st.error("Koneksi ke API Gagal. Pastikan .env Anda sudah benar.")
    st.stop() # Langsung berhenti

st.title("🌸 AI WAIFU Generate") 
st.write("Wujudkan halu anda menjadi WIAFU yang siap di tatap kapan saja") 

prompt = st.text_area(
    "Masukkan Prompt:",
    placeholder="Contoh: 'gadis anime rambut pink'"
)

submit_button = st.button(
    label="✨ Hasilkan Gambar"
)

if submit_button and prompt:
    st.info(f"Prompt yang dikirim: **{prompt}**") 

    try:
        # 3. Panggil API untuk Menghasilkan Gambar
        result = client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=dict(
                number_of_images=1,
                output_mime_type="image/png"
            )
        )

        if result.generated_images:
            # 4. Mendapatkan Data Gambar
            image_data = result.generated_images[0]
            image_bytes = image_data.image.image_bytes
            
            st.success("🎉 Gambar berhasil dibuat!")
            
            # 5. Menampilkan Gambar
            st.image(image_bytes, caption=f"Prompt: \"{prompt[:70]}...\"")
            
            # 6. Tombol Unduh Sederhana
            file_name = f'gambar_anime.png' # Nama file sederhana
            st.download_button(
                label="📥 Unduh Gambar",
                data=image_bytes,
                file_name=file_name,
                mime="image/png"
            )

        else:
            st.warning("⚠️ Gagal menghasilkan gambar. Coba ganti prompt Anda.")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

elif submit_button:
    st.warning("Harap masukkan prompt terlebih dahulu.")

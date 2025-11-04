import streamlit as st
import os
from openai import OpenAI
import requests  
from dotenv import load_dotenv
from datetime import datetime
import io

load_dotenv()

# Inisialisasi Klien GenAI
try:
    api_key = os.getenv('OPENAI_API_KEY') 
    
    if not api_key:
        st.error("Koneksi ke API Gagal. Pastikan nama Secret Anda adalah OPENAI_API_KEY.")
        st.stop()
        
    client = OpenAI(
        api_key=api_key
    )
except Exception as e:
    st.error(f"Gagal terhubung ke OpenAI: {e}")
    st.stop() 

st.title("🌸 AI WAIFU Generate") 
st.write("Wujudkan halu anda menjadi WAIFU yang siap di tatap kapan saja") 

prompt = st.text_area(
    "Masukkan Prompt:",
    placeholder="Contoh: 'gadis anime rambut pink'"
)

submit_button = st.button(
    label="✨ Hasilkan Gambar"
)
if submit_button and prompt:
    
    final_prompt = f"{prompt}, anime style, manga art, high quality, best quality"
    
    st.info(f"Prompt yang dikirim: **{final_prompt}**") 

    with st.spinner("Waifu anda sedang dibuat..."):
        try:
            # Model yang digunakan
            response = client.images.generate(
                model="dall-e-3",    
                prompt=final_prompt,
                size="1024x1024",    
                n=1,
                style="vivid"           
            )

            if response.data:
                image_url = response.data[0].url
                image_data = requests.get(image_url).content 
                
                st.success("🎉 Gambar berhasil dibuat!")
                
                # Menampilkan Gambar
                st.image(image_data, caption=f"Prompt: \"{prompt[:70]}...\"")
                
                #Tombol Unduh Sederhana
                file_name = f'gambar_anime.png'
                st.download_button(
                    label="📥 Unduh Gambar",
                    data=image_data,      
                    file_name=file_name,
                    mime="image/png"
                )

            else:
                st.warning("⚠️ Gagal menghasilkan gambar. Coba ganti prompt Anda.")

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

elif submit_button:
    st.warning("Harap masukkan prompt terlebih dahulu.")
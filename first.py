import streamlit as st
import urllib.parse
import requests

# إعدادات الصفحة الأساسية باسم البراند الفخم مالتك
st.set_page_config(
    page_title="MTR AURA", 
    page_icon="✨", 
    layout="centered"
)

# حقن كود التصميم الفخم (CSS)
style_code = """
<style>
    .stApp {
        background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 100%);
        color: #FFFFFF;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .brand-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(45deg, #FFE07D, #F5AF19);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        letter-spacing: 2px;
        filter: drop-shadow(0px 4px 10px rgba(245, 175, 25, 0.3));
    }
    .brand-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #B3B3B3;
        margin-bottom: 40px;
        font-weight: 300;
    }
    div.stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.07) !important;
        color: #FFFFFF !important;
        border: 2px solid rgba(245, 175, 25, 0.4) !important;
        border-radius: 25px !important;
        padding: 12px 25px !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease-in-out !important;
        text-align: center !important;
    }
    div.stTextInput > div > div > input:focus {
        border-color: #F5AF19 !important;
        box-shadow: 0 0 15px rgba(245, 175, 25, 0.6) !important;
        background-color: rgba(255, 255, 255, 0.12) !important;
    }
    
    .luxury-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 14px 20px;
        border-radius: 12px;
        font-weight: 600;
        text-decoration: none !important;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        margin-top: 15px;
        width: 100%;
        text-align: center;
    }
    .btn-gold {
        background: linear-gradient(45deg, #F5AF19, #E65C00);
        color: #000000 !important;
        box-shadow: 0 4px 15px rgba(245, 175, 25, 0.4);
    }
    .btn-gold:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(245, 175, 25, 0.7);
    }
    .btn-red {
        background: linear-gradient(45deg, #FF0000, #B30000);
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3);
    }
    .btn-red:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 0, 0, 0.5);
    }
    .btn-dark {
        background: rgba(255, 255, 255, 0.08);
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .btn-dark:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateY(-3px);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# الهيدر برأس الصفحة
st.markdown('<div class="brand-title">✨ MTR AURA ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-subtitle">سمفونية البحث والتحميل الموسيقي الفاخر</div>',st.markdown(f"""
    <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; margin-top: 25px; text-align: center;">
        <div style="font-size: 1.3rem; font-weight: 600; color: #FFFFFF; margin-bottom: 10px;">
            🎵 نتائج البحث عن: {song_name}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # زر التنزيل المباشر الفخم من نفس الصفحة والذي يقوم ببدء السحب الفوري بدون الانتقال لـ y2mate
    st.markdown(f'<a href="{direct_download_api}" target="_blank" class="luxury-btn btn-gold">🔥 (MP3) التحميل المباشر الفخم</a>', unsafe_allow_html=True)
    
    # الروابط الإضافية بستايل منسق وثابت
    st.markdown(f'<a href="{google_url}" target="_blank" class="luxury-btn btn-dark">🔍 بحث جوجل السريع</a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{youtube_url}" target="_blank" class="luxury-btn btn-red">📺 YouTube مشاهدة واستماع على</a>', unsafe_allow_html=True) unsafe_allow_html=True)

# خانة كتابة اسم الأغنية
song_name = st.text_input("", placeholder="اكتب اسم الأغنية أو الفنان هنا ثم اضغط Enter...")

if song_name:
    encoded_name = urllib.parse.quote(song_name)
    
    # روابط مساعدة ثابتة ومستقرة
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_name}"
    google_url = f"https://www.google.com/search?q={encoded_name}+song"
    
    # بوابة تنزيل سريعة ومباشرة تعمل أونلاين بكفاءة
    direct_download_api = f"https://api.vexdile.com/download?query={encoded_name}&format=mp3"

    # كارد النتيجة الفخم المدمج بالواجهة

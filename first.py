import streamlit as st
import urllib.parse
import os
import yt_dlp

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
    
    /* تصميم مخصص فخم لأزرار تحميل streamlit الافتراضية */
    div.stDownloadButton > button {
        background: linear-gradient(45deg, #F5AF19, #E65C00) !important;
        color: #000000 !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 14px 20px !important;
        border-radius: 12px !important;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(245, 175, 25, 0.4) !important;
        transition: all 0.3s ease !important;
        font-size: 1.1rem !important;
    }
    div.stDownloadButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 20px rgba(245, 175, 25, 0.7) !important;
    }
    
    /* روابط الاستماع الأخرى */
    .luxury-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 14px 20px;
        border-radius: 12px;
        font-weight: 600;
        text-decoration: none !important;
        font-size: 1rem;
        transition: all 0.3s ease;
        margin-top: 10px;
        width: 100%;
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
st.markdown('<div class="brand-subtitle">سمفونية البحث والتحميل الموسيقي الفاخر</div>', unsafe_allow_html=True)

# خانة كتابة اسم الأغنية
song_name = st.text_input("", placeholder="اكتب اسم الأغنية أو الفنان هنا ثم اضغط Enter...")

# دالة داخلية للبحث والتحميل المباشر بصيغة MP3 في الخلفية دون مغادرة الصفحة
def process_luxury_download(search_query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'default_search': 'ytsearch1', # جلب النتيجة الأولى تلقائياً من البحث
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=True)
        video_detail = info['entries'][0]
        title = video_detail['title']
        file_path = f"downloads/{title}.mp3"
        return file_path, title

if song_name:
    # إنشاء مجلد مؤقت للتحميلات إذا لم يكن موجوداً
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        
    encoded_name = urllib.parse.quote(song_name)
    
    # روابط إضافية للمشاهدة السريعة أو البحث العام كما كنت واضعها
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_name}"
    google_url = f"https://www.google.com/search?q={encoded_name}+song"

    with st.spinner("جاري جلب الملف الصوتي من السيرفرات الفخمة... 🎵"):
        try:
            # تشغيل معالجة الملف
            file_path, actual_song_title = process_luxury_download(song_name)
            
            # كارد عرض النتيجة المباشرة داخل الواجهة
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; margin-top: 25px; text-align: center;">
                <div style="font-size: 1.3rem; font-weight: 600; color: #FFFFFF; margin-bottom: 20px;">
                    🎵 نتائج البحث عن: {actual_song_title}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # قراءة الملف وعرضه في زر تحميل داخلي مباشر ومحمي
            with open(file_path, "rb") as audio_file:
                st.download_button(
                    label="🔥 (MP3) التحميل المباشر الفخم من نفس الصفحة",
                    data=audio_file,
                    file_name=f"{actual_song_title}.mp3",
                    mime="audio/mpeg"
                )
            
            # إضافة أزرار المساعدة المتبقية بالأسفل بستايل فخم متناسق مع الكود الأصلي
            st.markdown(f'<a href="{google_url}" target="_blank" class="luxury-btn btn-dark">🔍 بحث جوجل السريع</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{youtube_url}" target="_blank" class="luxury-btn btn-red">📺 YouTube مشاهدة واستماع على</a>', unsafe_allow_html=True)

        except Exception as e:
            st.error("عذراً، لم نتمكن من تنزيل الأغنية تلقائياً. يرجى التحقق من الاسم أو استخدام الروابط السريعة.")

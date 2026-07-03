import streamlit as st
import urllib.parse

# إعدادات الصفحة الأساسية (حدثناها بالاسم الفخم مالتك)
st.set_page_config(page_title="MTR AURA", page_icon="✨", layout="centered")

# تصميم الثيم الفخم (أسود ملكي وذهبي متوهج وتأثيرات زجاجية)
st.markdown("""
    <style>
    /* خلفية التطبيق بالكامل */
    .stApp {
        background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 100%);
        color: #FFFFFF;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* عنوان البراند الفخم */
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
    
    /* الشعار الفرعي */
    .brand-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #B3B3B3;
        margin-bottom: 40px;
        font-weight: 300;
    }
    
    /* حقل الإدخال الذهبي */
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
    
    /* بطاقة عرض النتائج الزجاجية الفاخرة */
    .music-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        margin-top: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
    }
    
    .song-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 25px;
    }
    
    /* شبكة الأزرار الاستجابة */
    .btn-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 15px;
    }
    
    @media (min-width: 600px) {
        .btn-grid {
            grid-template-columns: 1fr 1fr;
        }
    }
    
    /* تصميم الأزرار الفاخرة */
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
        cursor: pointer;
    }
    
    /* الزر الذهبي المشع للتحميل */
    .btn-gold {
        background: linear-gradient(45deg, #F5AF19, #E65C00);
        color: #000000 !important;
        box-shadow: 0 4px 15px rgba(245, 175, 25, 0.4);
    }
    
    .btn-gold:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(245, 175, 25, 0.7);
    }
    
    /* الزر المظلم الأنيق لجوجل */
    .btn-dark {
        background: rgba(255, 255, 255, 0.08);
        color: #FFFFFF !important;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .btn-dark:hover {
        background: rgba(255, 255, 255, 0.15);
        transform: translateY(-3px);
    }
    
    /* زر اليوتيوب الأحمر */
    .btn-red {
        background: linear-gradient(45deg, #FF0000, #B30000);
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3);
    }
    
    .btn-red:hover {
    transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 0, 0, 0.5);
    }
    
    /* إخفاء عناصر سترمليت الافتراضية المزعجة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# الهيدر الفخم برأس الصفحة
st.markdown('<div class="brand-title">✨ MTR AURA ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-subtitle">سمفونية البحث والتحميل الموسيقي الفاخر</div>', unsafe_allow_html=True)

# صندوق البحث الأنيق
query = st.text_input("", placeholder="اكتب اسم الأغنية أو الفنان هنا ثم اضغط Enter...")

if query:
    # تشفير النص لجعله آمناً للروابط
    encoded_query = urllib.parse.quote(query)
    
    # الروابط الذكية والحديثة بعد تحديث سيرفر التحميل
    yt_link = f"https://www.youtube.com/results?search_query={encoded_query}"
    google_link = f"https://www.google.com/search?q={encoded_query}+mp3"
    
    # استخدام السيرفر الحديث لـ Y2Mate الذي يبحث مباشرة بالكلمات
    mp3_direct_link = f"https://www.y2mate.com/search/{encoded_query}"
    
    # عرض بطاقة النتائج الفاخرة
    st.markdown(f"""
        <div class="music-card">
            <div class="song-title">🎵 نتائج البحث عن: {query}</div>
            <div class="btn-grid">
                <a href="{mp3_direct_link}" target="_blank" class="luxury-btn btn-gold">
                    🔥 التحميل المباشر الفخم (MP3)
                </a>
                <a href="{google_link}" target="_blank" class="luxury-btn btn-dark">
                    🔍 بحث جوجل السريع
                </a>
                <a href="{yt_link}" target="_blank" class="luxury-btn btn-red" style="grid-column: span 2;">
                    📺 مشاهدة واستماع على YouTube
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

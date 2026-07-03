import streamlit as st
import urllib.parse

# تهيئة إعدادات الصفحة وجعلها متوافقة مع الهواتف والحاسبات
st.set_page_config(
    page_title="MTR Aura | أورا الموسيقى",
    page_icon="✨",
    layout="centered",
)

# إضافة كود الـ CSS المخصص لخلق واجهة فاخرة جداً باللون المظلم والذهبي
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;800&display=swap');

/* تنسيق الخلفية العامة للموقع والخطوط */
.stApp {
    background: linear-gradient(135deg, #050811 0%, #0c1322 100%);
    font-family: 'Cairo', sans-serif;
    color: #f1f5f9;
}

/* تصميم ترويسة الصفحة الملكية */
.luxury-header {
    text-align: center;
    padding: 50px 0 30px 0;
}
.luxury-title {
    font-size: 3.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #f5e6be 0%, #d4af37 50%, #aa7c11 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 40px rgba(212, 175, 55, 0.25);
    margin-bottom: 5px;
    letter-spacing: 1.5px;
}
.luxury-subtitle {
    font-size: 1.15rem;
    color: #94a3b8;
    font-weight: 300;
    letter-spacing: 0.5px;
}

/* تنسيق صندوق البحث الجذاب والمتوهج بالذهبي */
div[data-testid="stTextInput"] > div {
    background: rgba(255, 255, 255, 0.02) !important;
    border: 1px solid rgba(212, 175, 55, 0.3) !important;
    border-radius: 50px !important;
    padding: 6px 24px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
    transition: all 0.3s ease-in-out !important;
}
div[data-testid="stTextInput"] > div:focus-within {
    border: 1px solid rgba(212, 175, 55, 0.8) !important;
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.35) !important;
}
div[data-testid="stTextInput"] input {
    color: #f8fafc !important;
    font-size: 1.15rem !important;
    text-align: center !important;
    font-family: 'Cairo', sans-serif !important;
}

/* تصميم بطاقة نتائج الموسيقى الزجاجية */
.music-card {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(212, 175, 55, 0.2);
    border-radius: 24px;
    padding: 35px;
    margin-top: 35px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    text-align: center;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.music-card:hover {
    border: 1px solid rgba(212, 175, 55, 0.5);
    box-shadow: 0 25px 60px rgba(212, 175, 55, 0.1);
    transform: translateY(-4px);
}

.song-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 25px;
}

/* أزرار التحميل الملكية وتوزيعها */
.btn-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 15px;
    margin-top: 15px;
}
@media (min-width: 600px) {
    .btn-grid {
        grid-template-columns: 1fr 1fr;
    }
}

.luxury-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 15px 25px;
    font-size: 1rem;
    font-weight: 700;
    border-radius: 15px;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    font-family: 'Cairo', sans-serif;
    gap: 10px;
}

/* زر التحميل الذهبي المشع */
.btn-gold {
    background: linear-gradient(135deg, #d4af37 0%, #aa7c11 100%);
    color: #050811 !important;
    box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
}
.btn-gold:hover {
    background: linear-gradient(135deg, #f5e6be 0%, #d4af37 100%);
    box-shadow: 0 6px 22px rgba(212, 175, 55, 0.55);
    transform: translateY(-2px);
}

/* زر البحث الثانوي الأنيق بحدود ذهبية */
.btn-dark {
    background: rgba(255, 255, 255, 0.03);
    color: #f5e6be !important;
    border: 1px solid rgba(212, 175, 55, 0.3);
}
.btn-dark:hover {
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid rgba(212, 175, 55, 0.8);
    transform: translateY(-2px);
}
/* زر اليوتيوب الأحمر الفخم */
.btn-red {
    background: rgba(239, 68, 68, 0.08);
    color: #fca5a5 !important;
    border: 1px solid rgba(239, 68, 68, 0.3);
}
.btn-red:hover {
    background: rgba(239, 68, 68, 0.2);
    border: 1px solid rgba(239, 68, 68, 0.8);
    transform: translateY(-2px);
}

/* إخفاء عناصر Streamlit الافتراضية لمنح مظهر التطبيقات الاحترافية */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# عرض ترويسة التطبيق بأسلوب فخم
st.markdown("""
<div class="luxury-header">
    <div class="luxury-title">✨ MTR AURA ✨</div>
    <div class="luxury-subtitle">سيمفونية البحث والتحميل الموسيقي الفاخر</div>
</div>
""", unsafe_allow_html=True)

# صندوق البحث الأنيق
query = st.text_input("", placeholder="اكتب اسم الأغنية أو الفنان هنا ثم اضغط Enter...")

if query:
    # تشفير النص لجعله آمناً للروابط
    encoded_query = urllib.parse.quote(query)
    
    # الروابط الذكية والسهلة
    yt_link = f"https://www.youtube.com/results?search_query={encoded_query}"
    google_link = f"https://www.google.com/search?q={encoded_query}+تحميل+mp3"
    mp3_direct_link = f"https://y2mate.is/en/search?q={encoded_query}"
    https://en.y2mate.is/s?q=%7Bencoded_query%7D
    # عرض بطاقة النتائج الفاخرة
    st.markdown(f"""
    <div class="music-card">
        <div class="song-title">🎵 نتائـج البحـث عـن: "{query}"</div>
        <div class="btn-grid">
            <a href="{mp3_direct_link}" target="_blank" class="luxury-btn btn-gold">
                ✨ التحميل المباشر الفخم (MP3)
            </a>
            <a href="{google_link}" target="_blank" class="luxury-btn btn-dark">
                🔍 بحث جوجل السريع
            </a>
            <a href="{yt_link}" target="_blank" class="luxury-btn btn-red" style="grid-column: span 2;">
                🎥 مشاهدة واستماع على YouTube
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

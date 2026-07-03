import streamlit as st
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="محرك بحث الأغاني", page_icon="🎵")

st.markdown("# 🔍 محرك البحث السريع عن الأغاني")
st.write("إكتب اسم الأغنية وهسة تطلعلك روابط الاستماع والتحميل المباشر!")

# خانة كتابة اسم الأغنية
song_name = st.text_input("اكتب اسم الأغنية أو الفنان هنا:")

if song_name:
    # تحويل النص إلى صيغة روابط الإنترنت
    encoded_name = urllib.parse.quote(song_name)
    
    # توليد روابط الاستماع والبحث العام
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_name}"
    google_url = f"https://www.google.com/search?q={encoded_name}+song"
    
    # توليد روابط تحميل MP3 مباشرة من محركات تحميل مشهورة
    mp3_download_url1 = f"https://www.google.com/search?q=تحميل+أغنية+{encoded_name}+mp3"
    mp3_download_url2 = f"https://www.mp3juices.cc/mp3/search?query={encoded_name}"

    st.markdown("### 🎧 روابط الاستماع المباشرة:")
    st.link_button("📺 فتح الأغنية مباشرة على YouTube", youtube_url)
    st.link_button("🌐 ابحث عن الأغنية وتفاصيلها على Google", google_url)
    
    st.write("---") # خط فاصل
    
    st.markdown("### 📥 أزرار التحميل المباشر بجهازك (MP3):")
    st.link_button("📥 تحميل الأغنية بصيغة MP3 (سريع)", mp3_download_url1)
    st.link_button("🎵 ابحث وحمل MP3 فوراً عبر MP3Juices", mp3_download_url2)
    
    st.success("🚀 اضغط على أزرار التحميل فوق وراح تنزل الأغنية بجهازك فوراً!")

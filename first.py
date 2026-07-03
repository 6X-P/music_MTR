import streamlit as st
import urllib.parse

st.title("🔍 محرك البحث السريع عن الأغاني")
st.write("اكتب اسم الأغنية وهسة نطلعلك رابطها المباشر!")

# خانة كتابة اسم الأغنية
song_name = st.text_input("اكتب اسم الأغنية أو الفنان هنا:")

if song_name:
    # تحويل النص إلى صيغة روابط الإنترنت (عشان الفراغات والكلمات العربية)
    encoded_name = urllib.parse.quote(song_name)
    
    # توليد روابط مباشرة لليوتيوب وللبحث العام
    youtube_url = f"https://www.youtube.com/results?search_query={encoded_name}"
    google_url = f"https://www.google.com/search?q={encoded_name}+song"
    
    st.markdown("### 🎧 روابط الاستماع المباشرة:")
    
    # أزرار ذكية تحول المستخدم للموقع فوراً
    st.link_button("📺 افتح الأغنية على YouTube مباشرة", youtube_url)
    st.link_button("🌐 ابحث عن الأغنية وتفاصيلها على Google", google_url)
    
    st.success("اضغط على الزر الفوق وراح يحولك للأغنية فوراً! 🚀")
import streamlit as st
import urllib.parse

# إعدادات الصفحة الأساسية باسم البراند الفخم مالتك
st.set_page_config(
    page_title="MTR AURA", 
    page_icon="✨", 
    layout="centered"
)

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
        border: 2px solid rgba(245, 175, 25,

if query:
    encoded_query = urllib.parse.quote(query)
    
    yt_link = f"https://www.youtube.com/results?search_query={encoded_query}"
    google_link = f"https://www.google.com/search?q={encoded_query}+mp3"
    mp3_direct_link = f"https://en.y2mate.is/s?q={encoded_query}"
    
    # بناء كرت النتائج بشكل آمن ومفصل
    card_html = f"""
    <div class="music-card">
        <div class="song-title">🎵 نتائج البحث عن: {query}</div>
        <div class="btn-grid">
            <a href="{mp3_direct_link}" target="_blank" class="luxury-btn btn-gold">
                🔥 التحميل المباشر الفخم (MP3)
            </a>
            <a href="{google_link}" target="_blank" class="luxury-btn btn-dark">
                🔍 بحث جوجل السريع
            </a>
            <a href="{yt_link}" target="_blank" class="luxury-btn btn-red">
                📺 مشاهدة واستماع على YouTube
            </a>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

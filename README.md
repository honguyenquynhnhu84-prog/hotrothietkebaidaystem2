import streamlit as st
import urllib.parse

def create_gemini_link(prompt_text):
    # Mã hóa nội dung prompt để đưa vào URL
    encoded_prompt = urllib.parse.quote(prompt_text)
    base_url = "https://gemini.google.com/app?prompt="
    return f"{base_url}{encoded_prompt}"

# --- Giao diện Streamlit ---
st.title("🚀 Trình tạo Link Prompt Gemini")

# Ô nhập liệu cho người dùng
user_prompt = st.text_area("Nhập nội dung prompt bạn muốn mẫu:", 
                           "Hãy đóng vai một chuyên gia Marketing và viết kế hoạch nội dung cho sản phẩm mới của tôi.")

if user_prompt:
    # Tạo đường link
    final_link = create_gemini_link(user_prompt)
    
    st.info("Khi nhấn nút dưới đây, Gemini sẽ mở ra và điền sẵn nội dung của bạn.")
    
    # Tạo nút bấm mở link
    st.link_button("Mở trong Gemini ✨", final_link)

    # Hiển thị link thô nếu cần (tùy chọn)
    with st.expander("Xem URL chi tiết"):
        st.code(final_link)
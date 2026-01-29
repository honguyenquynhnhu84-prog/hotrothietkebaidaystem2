import streamlit as st
import urllib.parse
st.set_page_config(page_title="Tên trang của bạn", layout="wide")

# Đoạn mã CSS để ẩn menu và footer của Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# Cấu hình trang
st.set_page_config(page_title="STEM Lesson Plan Generator", layout="wide")

st.title("🛠️ Chương trình hỗ trợ tạo Prompt thiết kế bài học STEM ")
st.info("Ứng dụng hỗ trợ giáo viên soạn thảo kế hoạch bài dạy STEM theo chuẩn Bộ GD&ĐT.")

# --- CẤU HÌNH CHUNG ---
st.header("⚙️ Cấu hình chung")
config_col1, config_col2, config_col3 = st.columns(3)

with config_col1:
    st.markdown("#### **Chọn khối lớp**")
    khoi_lop = st.selectbox("Chọn khối lớp", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"], label_visibility="collapsed")

with config_col2:
    st.markdown("#### **Chu trình dạy học**")
    chu_trinh = st.selectbox("Chu trình dạy học", ["Chu trình Kỹ thuật (EDP)", "Chu trình Khoa học"], label_visibility="collapsed")

with config_col3:
    st.markdown("#### **Thời lượng bài học**")
    thoi_luong = st.radio("Thời lượng bài học", ["1 tiết (45 phút)", "2 tiết (90 phút)"], label_visibility="collapsed")

st.divider()

# --- NỘI DUNG CHI TIẾT ---
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("#### **Tên bài dạy**")
    ten_bai = st.text_input("Tên bài dạy", placeholder="Ví dụ: Thiết kế mô hình đo chiều cao", label_visibility="collapsed")
    
    st.write("**Hoạt động cần soạn:**")
    hd1 = st.checkbox("HĐ 1: Xác định vấn đề", value=True)
    hd2 = st.checkbox("HĐ 2: Nghiên cứu kiến thức nền", value=True)
    hd3 = st.checkbox("HĐ 3: Lựa chọn giải pháp", value=True)
    hd4 = st.checkbox("HĐ 4: Chế tạo mẫu", value=True)
    hd5 = st.checkbox("HĐ 5: Đánh giá", value=True)
    
    # Tạo danh sách các hoạt động được chọn
    hd_chon = []
    if hd1: hd_chon.append("HĐ 1: Xác định vấn đề")
    if hd2: hd_chon.append("HĐ 2: Nghiên cứu kiến thức nền")
    if hd3: hd_chon.append("HĐ 3: Lựa chọn giải pháp")
    if hd4: hd_chon.append("HĐ 4: Chế tạo mẫu")
    if hd5: hd_chon.append("HĐ 5: Đánh giá")

with col2:
    st.markdown("#### **Kiến thức nền**")
    kien_thuc_nen = st.text_input("Kiến thức nền", placeholder="Ví dụ: Định lý Thales,...", label_visibility="collapsed")
    st.markdown("#### **Sản phẩm dự kiến**")
    san_pham = st.text_input("Sản phẩm dự kiến", placeholder="Ví dụ: Mô hình cây,...", label_visibility="collapsed")
    st.markdown("#### **Yêu cầu khác**")
    yeu_cau_khac = st.text_area("Yêu cầu khác", placeholder="(nếu có)", label_visibility="collapsed")

st.divider()

# --- TÙY CHỌN NÂNG CAO ---
st.header("📄 Tùy chọn nâng cao")
option_col1, option_col2, option_col3 = st.columns(3)

with option_col1:
    goi_y_vat_lieu = st.checkbox("Gợi ý vật liệu tái chế")

with option_col2:
    phu_luc = st.checkbox("Phụ lục (Phiếu học tập & Rubric)")

with option_col3:
    xuat_word = st.checkbox("Yêu cầu định dạng Word chuẩn")

st.divider()

# --- LOGIC TẠO PROMPT ---
if st.button("🔥 TẠO PROMPT VÀ LIÊN KẾT AI"):
    # Kiểm tra tên bài dạy
    if not ten_bai or ten_bai.strip() == "":
        st.error("⚠️ Vui lòng nhập tên bài dạy trước khi tạo prompt!")
        st.stop()
    
    # Xây dựng phần mục tiêu
    prompt_muc_tieu = """
    Mục tiêu bài học: Nêu rõ về kiến thức (Toán học là trọng tâm), kĩ năng, thái độ và năng lực đặc thù (năng lực giải quyết vấn đề, năng lực mô hình hóa toán học), năng lực số.
    """
    
    # Chi tiết từng hoạt động theo CV 3089
    hd_descriptions = {
        "HĐ 1: Xác định vấn đề": "HĐ 1: Xác định vấn đề: Giao nhiệm vụ thực tiễn dẫn đến nhu cầu giải quyết bằng toán học. Xác định rõ mục tiêu và các bước tiến hành.",
        "HĐ 2: Nghiên cứu kiến thức nền": "HĐ 2: Nghiên cứu kiến thức nền và đề xuất giải pháp: Học sinh tìm hiểu kiến thức toán học liên quan để giải quyết vấn đề. Xác định rõ mục tiêu và các bước tiến hành.",
        "HĐ 3: Lựa chọn giải pháp": "HĐ 3: Lựa chọn giải pháp/Thiết kế sản phẩm: Học sinh thảo luận, vẽ bản vẽ kỹ thuật hoặc lập kế hoạch tính toán. Xác định rõ mục tiêu và các bước tiến hành.",
        "HĐ 4: Chế tạo mẫu": "HĐ 4: Chế tạo mẫu, thử nghiệm và thảo luận: Thực hiện tính toán/chế tạo và điều chỉnh. Xác định rõ mục tiêu và các bước tiến hành.",
        "HĐ 5: Đánh giá": "HĐ 5: Chia sẻ, thảo luận và đánh giá: Thuyết trình về sản phẩm và ứng dụng toán học trong đó. Xác định rõ mục tiêu và các bước tiến hành."
    }
    
    selected_hds = "\n".join([hd_descriptions[h] for h in hd_chon])
    
    # Định dạng Word
    format_text = ""
    if xuat_word:
        format_text = "\nĐỊNH DẠNG VĂN BẢN: Trình bày nội dung phù hợp để copy vào Word với Font: Times New Roman, Cỡ chữ: 13, Căn lề: Đều hai bên (Justify), Tiêu đề: In đậm và viết hoa."

    # Tổng hợp toàn bộ Prompt
    full_prompt = f"""
Với vai trò là chuyên gia về giáo dục bạn hãy soạn giáo án STEM cho {khoi_lop} theo Công văn 3089/BGDĐT-GDTrH.
TÊN BÀI DẠY: {ten_bai.upper()}
CHU TRÌNH: {chu_trinh}
THỜI LƯỢNG: {thoi_luong}

{prompt_muc_tieu}

KIẾN THỨC NỀN: {kien_thuc_nen}
SẢN PHẨM DỰ KIẾN: {san_pham}

TIẾN TRÌNH DẠY HỌC (CHỈ SOẠN CÁC HOẠT ĐỘNG SAU):
{selected_hds}

YÊU CẦU BỔ SUNG:
{"- Tự động liệt kê danh sách vật liệu tái chế phù hợp." if goi_y_vat_lieu else ""}
{"- Thiết kế phụ lục phiếu học tập và bảng Rubric đánh giá sản phẩm." if phu_luc else ""}
- Thiết bị dạy học và học liệu: Liệt kê cụ thể.
{yeu_cau_khac}
{format_text}
    """

    # Hiển thị kết quả
    st.divider()
    st.subheader("📋 Kết quả Prompt")
    st.code(full_prompt, language="markdown")

    # --- NÚT LIÊN KẾT AI ---
    encoded_prompt = urllib.parse.quote(full_prompt)
    
    st.link_button("💬 Gửi sang ChatGPT", f"https://chatgpt.com/?q={encoded_prompt}", use_container_width=True)
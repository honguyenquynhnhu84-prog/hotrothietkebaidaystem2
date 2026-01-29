# 🛠️ Chương trình Hỗ trợ Tạo Prompt Thiết kế Bài học STEM

## 📖 Giới thiệu

Ứng dụng **Hỗ trợ Tạo Prompt Thiết kế Bài học STEM** là công cụ web được xây dựng bằng Streamlit, giúp giáo viên dễ dàng soạn thảo kế hoạch bài dạy STEM theo chuẩn **Công văn 3089/BGDĐT-GDTrH** của Bộ Giáo dục và Đào tạo Việt Nam.

Ứng dụng tự động tạo ra các prompt chi tiết, có cấu trúc để sử dụng với các công cụ AI như ChatGPT, giúp tiết kiệm thời gian và đảm bảo tính chuyên nghiệp trong việc thiết kế giáo án STEM.

## ✨ Tính năng chính

### 1. **Cấu hình bài học**
- Chọn khối lớp (Lớp 6, 7, 8, 9)
- Chọn chu trình dạy học (Chu trình Kỹ thuật EDP hoặc Chu trình Khoa học)
- Chọn thời lượng bài học (1 tiết hoặc 2 tiết)

### 2. **Nhập thông tin bài dạy**
- Tên bài dạy
- Kiến thức nền (các kiến thức toán học cần áp dụng)
- Sản phẩm dự kiến
- Yêu cầu bổ sung khác

### 3. **Lựa chọn hoạt động dạy học**
Chọn các hoạt động cần soạn theo chu trình STEM:
- HĐ 1: Xác định vấn đề
- HĐ 2: Nghiên cứu kiến thức nền
- HĐ 3: Lựa chọn giải pháp
- HĐ 4: Chế tạo mẫu
- HĐ 5: Đánh giá

### 4. **Tùy chọn nâng cao**
- Gợi ý vật liệu tái chế
- Tự động tạo phụ lục (Phiếu học tập & Rubric đánh giá)
- Định dạng Word chuẩn (Times New Roman, size 13, căn đều)

### 5. **Xuất kết quả**
- Tạo prompt chi tiết, có cấu trúc
- Hiển thị preview prompt ngay trên giao diện
- Liên kết trực tiếp sang ChatGPT với prompt đã được mã hóa

### 6. **Kiểm tra lỗi**
- Cảnh báo khi chưa nhập tên bài dạy
- Đảm bảo đầy đủ thông tin trước khi tạo prompt

## 🚀 Cài đặt và Chạy ứng dụng

### Yêu cầu hệ thống
- Python 3.7 trở lên
- pip (Python package manager)

### Các bước cài đặt

1. **Clone repository**
```bash
git clone https://github.com/honguyenquynhnhu84-prog/hotrothietkebaidaystem2.git
cd hotrothietkebaidaystem2
```

2. **Tạo môi trường ảo (khuyến nghị)**
```bash
python -m venv .venv
source .venv/bin/activate  # Trên Linux/Mac
# hoặc
.venv\Scripts\activate  # Trên Windows
```

3. **Cài đặt các thư viện cần thiết**
```bash
pip install -r requirements.txt
```

4. **Chạy ứng dụng**
```bash
streamlit run streamlit_app.py
```

5. **Truy cập ứng dụng**
- Mở trình duyệt và truy cập: `http://localhost:8501`

## 📱 Hướng dẫn sử dụng

### Bước 1: Cấu hình chung
1. Chọn **khối lớp** phù hợp với đối tượng học sinh
2. Chọn **chu trình dạy học** (Kỹ thuật hoặc Khoa học)
3. Chọn **thời lượng bài học** (1 tiết hoặc 2 tiết)

### Bước 2: Nhập thông tin bài dạy
1. **Tên bài dạy**: Nhập tên cụ thể của bài học (bắt buộc)
   - Ví dụ: "Thiết kế mô hình đo chiều cao"
   
2. **Hoạt động cần soạn**: Chọn các hoạt động muốn AI soạn thảo chi tiết

3. **Kiến thức nền**: Nhập các kiến thức toán học liên quan
   - Ví dụ: "Định lý Thales, Tỉ lệ thức"
   
4. **Sản phẩm dự kiến**: Mô tả sản phẩm học sinh sẽ tạo ra
   - Ví dụ: "Mô hình cây đo chiều cao bằng que"
   
5. **Yêu cầu khác**: Bổ sung các yêu cầu đặc biệt (nếu có)

### Bước 3: Tùy chọn nâng cao
- ✅ **Gợi ý vật liệu tái chế**: AI sẽ đề xuất vật liệu từ môi trường
- ✅ **Phụ lục**: Tự động tạo phiếu học tập và bảng Rubric
- ✅ **Định dạng Word chuẩn**: Đảm bảo format phù hợp để copy vào Word

### Bước 4: Tạo và sử dụng Prompt
1. Nhấn nút **"🔥 TẠO PROMPT VÀ LIÊN KẾT AI"**
2. Xem preview prompt ngay trên giao diện
3. Nhấn nút **"💬 Gửi sang ChatGPT"** để mở ChatGPT với prompt đã điền sẵn
4. Đợi AI tạo nội dung giáo án hoàn chỉnh

## 🎯 Ví dụ minh họa

### Đầu vào mẫu:
- **Khối lớp**: Lớp 8
- **Chu trình**: Chu trình Kỹ thuật (EDP)
- **Thời lượng**: 2 tiết (90 phút)
- **Tên bài dạy**: Thiết kế mô hình cầu tre
- **Kiến thức nền**: Định lý Pythagore, Lực và mô men lực
- **Sản phẩm**: Mô hình cầu tre thu nhỏ

### Đầu ra:
Prompt chi tiết với đầy đủ cấu trúc theo CV 3089, bao gồm:
- Mục tiêu bài học (kiến thức, kỹ năng, thái độ, năng lực)
- Tiến trình dạy học chi tiết cho từng hoạt động
- Danh sách thiết bị và học liệu
- Phụ lục và rubric đánh giá (nếu chọn)

## 📂 Cấu trúc dự án

```
hotrothietkebaidaystem2/
├── streamlit_app.py      # File chính chứa code ứng dụng
├── requirements.txt      # Danh sách thư viện Python cần thiết
├── README.md            # File hướng dẫn (file này)
└── LICENSE              # Giấy phép sử dụng
```

## 🔧 Công nghệ sử dụng

- **Streamlit**: Framework web app cho Python
- **Python 3.x**: Ngôn ngữ lập trình chính
- **urllib**: Mã hóa URL cho ChatGPT API

## 📝 Lưu ý

- Ứng dụng cần kết nối internet để truy cập ChatGPT
- Prompt được tạo ra tuân thủ chuẩn CV 3089/BGDĐT-GDTrH
- Nên kiểm tra và chỉnh sửa nội dung AI tạo ra cho phù hợp với tình hình thực tế của lớp học

## 🤝 Đóng góp

Mọi đóng góp, báo lỗi hoặc đề xuất tính năng mới đều được hoan nghênh! 

Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/TenTinhNang`)
3. Commit thay đổi (`git commit -m 'Thêm tính năng mới'`)
4. Push lên branch (`git push origin feature/TenTinhNang`)
5. Tạo Pull Request

## 📧 Liên hệ

- **Repository**: [hotrothietkebaidaystem2](https://github.com/honguyenquynhnhu84-prog/hotrothietkebaidaystem2)
- **Tác giả**: honguyenquynhnhu84-prog

## 📄 Giấy phép

Dự án này được phát hành dưới giấy phép mã nguồn mở. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

**Phát triển với ❤️ để hỗ trợ giáo viên Việt Nam**
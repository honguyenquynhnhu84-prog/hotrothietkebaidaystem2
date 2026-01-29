# 📚 HƯỚNG DẪN SỬ DỤNG CHI TIẾT

## 🎯 Mục đích

Tài liệu này hướng dẫn chi tiết cách sử dụng ứng dụng **Hỗ trợ Tạo Prompt Thiết kế Bài học STEM** từ A đến Z, phù hợp cho giáo viên bất kỳ trình độ công nghệ nào.

---

## 📋 Mục lục

1. [Khởi động ứng dụng](#1-khởi-động-ứng-dụng)
2. [Giao diện tổng quan](#2-giao-diện-tổng-quan)
3. [Hướng dẫn từng bước](#3-hướng-dẫn-từng-bước)
4. [Các tình huống sử dụng](#4-các-tình-huống-sử-dụng)
5. [Xử lý lỗi thường gặp](#5-xử-lý-lỗi-thường-gặp)
6. [Mẹo và thủ thuật](#6-mẹo-và-thủ-thuật)

---

## 1. Khởi động ứng dụng

### Cách 1: Sử dụng trực tuyến (Khuyến nghị)
- Truy cập link ứng dụng (nếu đã deploy)
- Không cần cài đặt gì thêm

### Cách 2: Chạy trên máy tính cá nhân

**Bước 1**: Mở Terminal/Command Prompt

**Bước 2**: Di chuyển đến thư mục chứa code
```bash
cd đường_dẫn_đến_thư_mục/hotrothietkebaidaystem2
```

**Bước 3**: Chạy lệnh
```bash
streamlit run streamlit_app.py
```

**Bước 4**: Mở trình duyệt tại địa chỉ hiển thị (thường là `http://localhost:8501`)

---

## 2. Giao diện tổng quan

Ứng dụng được chia thành các phần chính:

```
┌─────────────────────────────────────────────┐
│   🛠️ CHƯƠNG TRÌNH HỖ TRỢ TẠO PROMPT       │
│   THIẾT KẾ BÀI HỌC STEM                    │
└─────────────────────────────────────────────┘

┌─────────────────────────────────────────────┐
│  ⚙️ CẤU HÌNH CHUNG                         │
│  [Khối lớp] [Chu trình] [Thời lượng]       │
└─────────────────────────────────────────────┘

┌──────────────────────┬──────────────────────┐
│  NỘI DUNG BÀI HỌC   │  THÔNG TIN BỔ SUNG   │
│  - Tên bài dạy       │  - Kiến thức nền     │
│  - Hoạt động soạn    │  - Sản phẩm dự kiến  │
│                      │  - Yêu cầu khác      │
└──────────────────────┴──────────────────────┘

┌─────────────────────────────────────────────┐
│  📄 TÙY CHỌN NÂNG CAO                      │
│  ☐ Vật liệu tái chế                        │
│  ☐ Phụ lục & Rubric                        │
│  ☐ Định dạng Word chuẩn                    │
└─────────────────────────────────────────────┘

          [🔥 TẠO PROMPT VÀ LIÊN KẾT AI]
```

---

## 3. Hướng dẫn từng bước

### Bước 1️⃣: Cấu hình chung

#### 1.1. Chọn khối lớp
- Nhấn vào menu dropdown **"Chọn khối lớp"**
- Chọn: Lớp 6, Lớp 7, Lớp 8, hoặc Lớp 9
- **Lưu ý**: Khối lớp ảnh hưởng đến mức độ kiến thức trong giáo án

#### 1.2. Chọn chu trình dạy học
Có 2 lựa chọn:

**Chu trình Kỹ thuật (EDP)**:
- Phù hợp với bài dạy thiết kế, chế tạo sản phẩm
- Tập trung vào Engineering Design Process
- Ví dụ: Thiết kế cầu, chế tạo robot, xây dựng mô hình

**Chu trình Khoa học**:
- Phù hợp với bài dạy nghiên cứu, thí nghiệm
- Tập trung vào phương pháp khoa học
- Ví dụ: Nghiên cứu độ pH, thí nghiệm vật lý

#### 1.3. Chọn thời lượng
- **1 tiết (45 phút)**: Bài học ngắn, tập trung một vấn đề cụ thể
- **2 tiết (90 phút)**: Bài học đầy đủ với nhiều hoạt động

---

### Bước 2️⃣: Nhập thông tin bài dạy

#### 2.1. Tên bài dạy (BẮT BUỘC ⚠️)
- Nhập tên cụ thể, rõ ràng cho bài học
- **Ví dụ tốt**: 
  - ✅ "Thiết kế mô hình cầu treo thu nhỏ"
  - ✅ "Nghiên cứu ứng dụng định lý Pythagore trong đo đạc"
- **Ví dụ không tốt**:
  - ❌ "Toán học" (quá chung chung)
  - ❌ "Bài 1" (không rõ nội dung)

#### 2.2. Chọn hoạt động cần soạn
Chọn các checkbox tương ứng với hoạt động muốn AI soạn chi tiết:

| Hoạt động | Nội dung | Khi nào cần? |
|-----------|----------|--------------|
| HĐ 1 | Xác định vấn đề | Luôn chọn - mở đầu bài học |
| HĐ 2 | Nghiên cứu kiến thức nền | Bài có kiến thức toán học nền tảng |
| HĐ 3 | Lựa chọn giải pháp | Bài thiết kế, so sánh phương án |
| HĐ 4 | Chế tạo mẫu | Bài thực hành, làm sản phẩm |
| HĐ 5 | Đánh giá | Luôn chọn - kết thúc bài học |

**Mẹo**: Bài học hoàn chỉnh nên chọn cả 5 hoạt động

#### 2.3. Kiến thức nền
Liệt kê các kiến thức toán học học sinh cần vận dụng:
- **Ví dụ 1**: "Định lý Pythagore, Căn bậc hai"
- **Ví dụ 2**: "Tỉ lệ thức, Thang tỉ lệ"
- **Ví dụ 3**: "Hệ phương trình bậc nhất, Đồ thị hàm số"

#### 2.4. Sản phẩm dự kiến
Mô tả cụ thể sản phẩm học sinh sẽ tạo ra:
- **Ví dụ 1**: "Mô hình cầu treo bằng tre và dây thép"
- **Ví dụ 2**: "Bản vẽ thiết kế nhà ở với tính toán diện tích"
- **Ví dụ 3**: "Báo cáo nghiên cứu ứng dụng toán học trong đời sống"

#### 2.5. Yêu cầu khác (Tùy chọn)
Bổ sung các yêu cầu đặc biệt:
- "Tích hợp công nghệ số (sử dụng Geogebra)"
- "Phù hợp với học sinh khuyết tật"
- "Kết hợp với môn Vật lý về lực"

---

### Bước 3️⃣: Tùy chọn nâng cao

#### 3.1. ☐ Gợi ý vật liệu tái chế
- **Khi chọn**: AI sẽ đề xuất danh sách vật liệu từ môi trường, tái chế
- **Phù hợp**: Bài dạy có chế tạo sản phẩm, bảo vệ môi trường
- **Ví dụ output**: "Chai nhựa, hộp sữa, que tre, dây thép phế thải..."

#### 3.2. ☐ Phụ lục (Phiếu học tập & Rubric)
- **Khi chọn**: AI tạo thêm:
  - Phiếu học tập cho học sinh điền
  - Bảng Rubric đánh giá sản phẩm chi tiết
- **Khuyến nghị**: Luôn chọn để giáo án hoàn chỉnh

#### 3.3. ☐ Yêu cầu định dạng Word chuẩn
- **Khi chọn**: Nội dung được format sẵn theo quy chuẩn:
  - Font: Times New Roman
  - Size: 13
  - Căn lề: Đều hai bên (Justify)
  - Tiêu đề: In đậm và viết hoa
- **Khuyến nghị**: Chọn nếu cần nộp giáo án chính thức

---

### Bước 4️⃣: Tạo và sử dụng Prompt

#### 4.1. Nhấn nút "TẠO PROMPT"
- Kiểm tra lại thông tin đã nhập
- Nhấn nút **"🔥 TẠO PROMPT VÀ LIÊN KẾT AI"**

#### 4.2. Xem Preview
- Prompt sẽ hiển thị trong khung màu xám
- Đọc qua để kiểm tra độ chính xác
- Có thể copy thủ công nếu muốn

#### 4.3. Gửi sang ChatGPT
- Nhấn nút **"💬 Gửi sang ChatGPT"**
- Trình duyệt mới mở ra với ChatGPT
- Prompt đã được điền sẵn
- Nhấn Enter hoặc nút gửi trong ChatGPT
- Đợi AI tạo nội dung (thường 30-60 giây)

#### 4.4. Xử lý kết quả từ AI
- Copy toàn bộ nội dung AI tạo ra
- Dán vào Word hoặc Google Docs
- Đọc kỹ và chỉnh sửa cho phù hợp với lớp học
- Lưu file giáo án

---

## 4. Các tình huống sử dụng

### Tình huống 1: Bài dạy thiết kế sản phẩm đơn giản (45 phút)

**Mục tiêu**: Học sinh lớp 6 thiết kế hộp đựng bút bằng bìa carton

**Cấu hình**:
- Khối lớp: Lớp 6
- Chu trình: Chu trình Kỹ thuật (EDP)
- Thời lượng: 1 tiết (45 phút)
- Tên bài: "Thiết kế hộp đựng bút từ bìa carton"
- Hoạt động chọn: HĐ 1, HĐ 3, HĐ 4
- Kiến thức nền: "Diện tích hình chữ nhật, chu vi"
- Sản phẩm: "Hộp đựng bút bằng bìa carton tái chế"
- Tùy chọn: ✅ Vật liệu tái chế, ✅ Rubric

---

### Tình huống 2: Bài dạy nghiên cứu chuyên sâu (90 phút)

**Mục tiêu**: Học sinh lớp 9 nghiên cứu ứng dụng hàm số bậc hai

**Cấu hình**:
- Khối lớp: Lớp 9
- Chu trình: Chu trình Khoa học
- Thời lượng: 2 tiết (90 phút)
- Tên bài: "Nghiên cứu quỹ đạo chuyển động ném xiên"
- Hoạt động chọn: Cả 5 hoạt động
- Kiến thức nền: "Hàm số bậc hai, Parabol"
- Sản phẩm: "Báo cáo nghiên cứu với đồ thị và số liệu thực nghiệm"
- Tùy chọn: ✅ Rubric, ✅ Định dạng Word

---

### Tình huống 3: Bài dạy tích hợp liên môn

**Mục tiêu**: Lớp 8 thiết kế cầu treo kết hợp Toán-Vật lý

**Cấu hình**:
- Khối lớp: Lớp 8
- Chu trình: Chu trình Kỹ thuật (EDP)
- Thời lượng: 2 tiết (90 phút)
- Tên bài: "Thiết kế mô hình cầu treo ứng dụng Định lý Pythagore"
- Hoạt động chọn: Cả 5 hoạt động
- Kiến thức nền: "Định lý Pythagore, Tỉ lệ thức, Lực và mômen lực"
- Sản phẩm: "Mô hình cầu treo thu nhỏ có thể chịu tải"
- Yêu cầu khác: "Kết hợp với môn Vật lý phần Lực"
- Tùy chọn: ✅ Vật liệu tái chế, ✅ Rubric, ✅ Word

---

## 5. Xử lý lỗi thường gặp

### ❌ Lỗi: "Vui lòng nhập tên bài dạy"

**Nguyên nhân**: Chưa điền thông tin vào ô "Tên bài dạy"

**Giải quyết**: 
1. Cuộn lên phần "Tên bài dạy"
2. Nhập tên cụ thể cho bài học
3. Nhấn lại nút "TẠO PROMPT"

---

### ❌ Lỗi: ChatGPT không mở

**Nguyên nhân**: Trình duyệt chặn popup hoặc không có kết nối internet

**Giải quyết**:
1. Kiểm tra kết nối internet
2. Cho phép popup từ ứng dụng trong trình duyệt
3. Hoặc: Copy prompt thủ công và dán vào ChatGPT

---

### ❌ Lỗi: Nội dung AI tạo ra không đúng

**Nguyên nhân**: Thông tin đầu vào chưa đủ cụ thể

**Giải quyết**:
1. Điền đầy đủ hơn các trường thông tin
2. Cụ thể hóa "Kiến thức nền" và "Sản phẩm"
3. Bổ sung "Yêu cầu khác" để làm rõ mong muốn
4. Tạo lại prompt với thông tin đầy đủ hơn

---

### ❌ Lỗi: Ứng dụng không chạy

**Nguyên nhân**: Chưa cài đặt đúng thư viện

**Giải quyết**:
```bash
pip install --upgrade streamlit
pip install -r requirements.txt
```

---

## 6. Mẹo và thủ thuật

### 💡 Mẹo 1: Tái sử dụng prompt
- Copy prompt đã tạo và lưu vào file .txt
- Chỉnh sửa một chút cho bài học tương tự
- Tiết kiệm thời gian cho các bài học có cấu trúc giống nhau

### 💡 Mẹo 2: Kết hợp nhiều AI
- Tạo prompt trong ứng dụng
- Sử dụng cho nhiều AI khác nhau:
  - ChatGPT
  - Google Gemini
  - Claude AI
- So sánh và chọn kết quả tốt nhất

### 💡 Mẹo 3: Tùy chỉnh sau khi tạo
- Không cần phải hoàn hảo ngay từ đầu
- Tạo prompt cơ bản trước
- Sau khi AI trả về, yêu cầu tiếp:
  - "Làm chi tiết hơn phần HĐ 2"
  - "Thêm câu hỏi dẫn dắt cho học sinh"
  - "Điều chỉnh cho phù hợp với học sinh yếu"

### 💡 Mẹo 4: Lưu giữ tốt
Tạo thư mục quản lý:
```
Giáo án STEM/
├── Lớp 6/
│   ├── Bài 1 - Thiết kế hộp đựng bút.docx
│   ├── Bài 1 - Prompt gốc.txt
├── Lớp 7/
├── Lớp 8/
└── Lớp 9/
```

### 💡 Mẹo 5: Chia sẻ với đồng nghiệp
- Tạo prompt cho bài học chung
- Chia sẻ link ứng dụng với tổ chuyên môn
- Cùng nhau xây dựng thư viện giáo án STEM

### 💡 Mẹo 6: Feedback để AI học
Sau khi sử dụng giáo án thực tế:
- Ghi chú lại phần nào hiệu quả, phần nào cần sửa
- Lần sau tạo prompt tương tự, bổ sung yêu cầu cụ thể hơn
- Ví dụ: "Tạo nhiều câu hỏi dẫn dắt hơn ở HĐ 1"

---

## ❓ Câu hỏi thường gặp (FAQ)

**Q1: Tôi có cần tài khoản ChatGPT trả phí không?**
- A: Không. Tài khoản miễn phí vẫn sử dụng được.

**Q2: Prompt có phù hợp với tất cả các môn STEM không?**
- A: Prompt tập trung vào Toán học. Nếu muốn tích hợp môn khác, ghi rõ trong "Yêu cầu khác".

**Q3: Tôi có thể chỉnh sửa prompt trước khi gửi không?**
- A: Có. Copy prompt, chỉnh sửa, rồi dán thủ công vào ChatGPT.

**Q4: Giáo án AI tạo có chuẩn không?**
- A: Cấu trúc chuẩn theo CV 3089. Nội dung cần giáo viên kiểm tra và điều chỉnh cho phù hợp.

**Q5: Có giới hạn số lần sử dụng không?**
- A: Không giới hạn với ứng dụng. ChatGPT miễn phí có thể giới hạn số câu hỏi/ngày.

---

## 📞 Hỗ trợ

Nếu gặp khó khăn:
1. Đọc lại hướng dẫn này
2. Kiểm tra phần "Xử lý lỗi thường gặp"
3. Liên hệ qua GitHub Issues

---

**Chúc bạn soạn giáo án hiệu quả! 🎓✨**
# 🧠 Handwritten Character & Digit Recognition (0-9 + A-Z)

Dự án này xây dựng một hệ thống nhận dạng chữ cái và chữ số viết tay (0–9, A–Z) bằng cách huấn luyện mô hình CNN trên dữ liệu kết hợp từ **MNIST** và **A-Z Handwritten Data**.

---

## 📁 Cấu trúc dự án


├── datas/
│   ├── mnist_dataset/                   
│   └── A_Z Handwritten Data.csv       
│
├── .venv/  
│
├── model/
│	└── model_char_digit_36class.h5 
│
├── src/                   
│   └── train.py
│
├── test/                   
│   └── train.py
│
├── train_model.py            
├── predict_example.py        
├── requirements.txt           
└── README.md              


---

## 📚 Dữ liệu sử dụng

- **MNIST**: Tập dữ liệu ảnh số viết tay từ 0–9, kích thước 28x28, ảnh đen trắng.
- **A-Z Handwritten Data**: Dữ liệu chữ cái viết tay từ A đến Z, lưu ở dạng CSV, gồm **372.450** ảnh 28x28.

---

## 🏗️ Mô hình

- **Kiến trúc**: Mạng nơ-ron tích chập (CNN) gồm 2 khối `Conv2D + MaxPooling + Dropout` → `Flatten` → `Dense`.
- **Số lớp đầu ra**: 36 lớp (0–9 và A–Z).
- **Hàm mất mát**: `categorical_crossentropy`.
- **Đánh giá**: Độ chính xác (`accuracy`) trên tập validation.

---

## 🧪 Huấn luyện mô hình

Chạy đoạn mã sau để huấn luyện:
```bash
python train_model.py


Sau khi huấn luyện xong, mô hình sẽ được lưu tại:  
📁 `model/model_char_digit_36class.h5`

---

## 🔍 Dự đoán ảnh mới

Dự đoán ký tự viết tay từ ảnh PNG:
```bash
python predict_example.py --image path/to/image.png


Quy trình xử lý ảnh đầu vào:

- Chuyển ảnh sang **đen trắng**.
- Resize về **28x28**.
- **Normalize** dữ liệu ảnh.
- Dự đoán và hiển thị kết quả bằng `matplotlib`.

---

## 🔠 Mã hóa nhãn

| Label | Ký tự |
|-------|-------|
| 0–9   | 0–9   |
| 10–35 | A–Z   |

---

## 📦 Cài đặt yêu cầu

Cài đặt thư viện cần thiết:
```bash
pip install -r requirements.txt


---

## 📌 Ghi chú

- Hãy đảm bảo rằng file `A_Z Handwritten Data.csv` và thư mục `mnist_dataset` nằm cùng cấp với các script Python.
- Dự án này chỉ xử lý ảnh **đơn ký tự**.

---

## 🚀 Tác giả

Dự án được phát triển bởi **[DoNhi]** nhằm mục đích **học tập, thử nghiệm AI và thị giác máy tính (computer vision)**.

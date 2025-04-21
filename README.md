# 🧠 Handwritten Character & Digit Recognition (0-9 + A-Z)

Dự án này xây dựng một hệ thống nhận dạng chữ cái và chữ số viết tay (0–9, A–Z) bằng cách huấn luyện mô hình CNN trên dữ liệu kết hợp từ **MNIST** và **A-Z Handwritten Letters**.

---

## 📁 Cấu trúc dự án

. ├── mnist_dataset/ │ ├── train/ # Ảnh train (từ MNIST) │ ├── test/ # Ảnh test (từ MNIST) │ ├── train_labels.csv # Nhãn train │ └── test_labels.csv # Nhãn test ├── A_Z Handwritten Data.csv # Dữ liệu chữ viết tay A-Z ├── model_char_digit_36class.h5 # Mô hình đã huấn luyện ├── predict_example.py # Script dự đoán ảnh mới ├── train_model.py # Script huấn luyện mô hình └── README.md

---

## 📚 Dữ liệu sử dụng

- **MNIST**: tập dữ liệu ảnh số viết tay 0–9, ảnh 28x28, trắng đen.
- **A-Z Handwritten Data**: CSV chứa ảnh viết tay chữ cái từ A đến Z (ảnh 28x28, 372.450 mẫu).

---

## 🏗️ Mô hình

- **Kiến trúc**: CNN gồm 2 khối Conv2D + MaxPooling + Dropout → Dense.
- **Số lớp đầu ra**: 36 lớp tương ứng với 0–9 và A–Z.
- **Hàm mất mát**: categorical crossentropy.
- **Đánh giá**: độ chính xác trên tập validation.

---

## 🧪 Cách chạy huấn luyện

> Huấn luyện mô hình từ dữ liệu đã gộp:

```bash
python train_model.py

🔍 Dự đoán ảnh mới
Dự đoán ký tự từ ảnh PNG bất kỳ (ảnh trắng đen, 28x28 hoặc tự động resize):

python predict_example.py --image path/to/image.png
Ảnh đầu vào sẽ được:

Chuyển về ảnh trắng đen.

Resize về 28x28.

Chuẩn hóa (normalize).

Dự đoán và hiển thị kết quả bằng matplotlib.
🔠 Mã hóa nhãn

Label	Ký tự
0–9	0–9
10–35	A–Z
📦 Yêu cầu
pip install -r requirements.txt
📌 Ghi chú
Bạn cần đặt file A_Z Handwritten Data.csv và thư mục mnist_dataset cùng cấp với script.

Model sau khi huấn luyện sẽ được lưu thành model_char_digit_36class.h5.
🚀 Tác giả
Dự án xây dựng bởi [Tên của bạn] – nhằm mục đích học tập và thử nghiệm AI nhận dạng ảnh.

---

Bạn muốn mình tạo luôn các file `train_model.py`, `predict_example.py` và `requirements.txt` tương ứng để bạn có thể chạy cả dự án như một project Python hoàn chỉnh không?


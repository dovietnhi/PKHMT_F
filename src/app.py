import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
from tensorflow.keras.models import load_model

# Load mô hình đã lưu
model = load_model(r'F:\DAKHMT\PKHMT_F\model\model_char_digit_36class.h5')

# Kích thước ảnh vẽ và đầu vào
CANVAS_SIZE = 280
IMG_SIZE = 28

# Tạo cửa sổ chính
root = tk.Tk()
root.title("✍️ Nhận dạng chữ viết tay thông minh")
root.geometry("600x400")
root.configure(bg="#f0f4f8")

# Tiêu đề
title = tk.Label(root, text="📖 Viết tay & Dự đoán (0-9, A-Z)", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#333")
title.pack(pady=10)

# Canvas vẽ
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white", bd=2, relief="ridge")
canvas.place(x=40, y=60)

# Ảnh để vẽ
image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), "white")
draw = ImageDraw.Draw(image)

def paint(event):
    x, y = event.x, event.y
    r = 12
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")
    draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

canvas.bind("<B1-Motion>", paint)

# Kết quả dự đoán
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 18), bg="#f0f4f8", fg="#007acc")
result_label.place(x=350, y=100)

# Hàm xóa canvas
def clear_canvas():
    canvas.delete("all")
    draw.rectangle([0, 0, CANVAS_SIZE, CANVAS_SIZE], fill="white")
    result_var.set("")

# Hàm dự đoán chữ viết
def predict():
    # Resize ảnh và chuẩn hóa
    img_resized = image.resize((IMG_SIZE, IMG_SIZE))
    img_invert = ImageOps.invert(img_resized)
    img_arr = np.array(img_invert).astype("float32") / 255.0
    img_arr = img_arr.reshape(1, IMG_SIZE, IMG_SIZE, 1)

    # Dự đoán
    pred = model.predict(img_arr)
    pred_class = np.argmax(pred[0])

    if pred_class < 10:
        result = f"🔢 Số: {pred_class}"
    else:
        result = f"🔤 Chữ cái: {chr(pred_class - 10 + ord('A'))}"

    result_var.set(f"Kết quả: {result}")

# Nút dự đoán
predict_btn = ttk.Button(root, text="📌 Dự đoán", command=predict)
predict_btn.place(x=370, y=180)

# Nút xóa
clear_btn = ttk.Button(root, text="🧹 Xóa", command=clear_canvas)
clear_btn.place(x=370, y=220)

# Chạy ứng dụng
root.mainloop()

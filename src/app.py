import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageOps, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
import time

# Tải mô hình
model = load_model(r'F:\DAKHMT\PKHMT_F\src\best_deepcnn_model.h5')

CANVAS_SIZE = 280
IMG_SIZE = 28
CLASSES = [str(i) for i in range(10)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Giao diện chính
root = tk.Tk()
root.title("✍️ Nhận dạng chữ viết tay")
root.geometry("1100x400")
root.configure(bg="white")

# Canvas vẽ
canvas = tk.Canvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE, bg="white", bd=2, relief="ridge")
canvas.place(x=50, y=40)

# Ảnh nền để vẽ
image = Image.new("L", (CANVAS_SIZE, CANVAS_SIZE), "white")
draw = ImageDraw.Draw(image)

def paint(event):
    x, y = event.x, event.y
    r = 12
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")
    draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

canvas.bind("<B1-Motion>", paint)

# Ảnh đã xử lý
processed_label = tk.Label(root, bd=2, relief="ridge")
processed_label.place(x=370, y=40, width=CANVAS_SIZE, height=CANVAS_SIZE)

# Kết quả
output_frame = tk.Frame(root, bg="white")
output_frame.place(x=700, y=40, width=350, height=240)

output_text = tk.Label(output_frame, text="OUTPUT", font=("Helvetica", 12, "bold"), bg="white")
output_text.grid(row=0, column=0, pady=5)

pred_label = tk.Label(output_frame, text="", font=("Helvetica", 24, "bold"), fg="black", bg="white")
pred_label.grid(row=1, column=0, pady=10)
percent_label = tk.Label(output_frame, text="0%", font=("Helvetica", 10, "bold"), fg="blue", bg="white")

# Thanh dự đoán và phần trăm
bars = []
labels = []
percent_labels = []
percent_desc_labels = []  # Thêm phần mô tả cho phần trăm

for i in range(3):
    label = tk.Label(output_frame, text="", font=("Helvetica", 12), bg="#eee", width=3)
    label.grid(row=2 + i, column=0, pady=5)
    bar = ttk.Progressbar(output_frame, orient="horizontal", length=120, mode="determinate")
    bar.grid(row=2 + i, column=1, padx=5)
    percent_label = tk.Label(output_frame, text="0%", font=("Helvetica", 10), bg="white")
    percent_label.grid(row=2 + i, column=2, padx=5)
    percent_desc_label = tk.Label(output_frame, text=f"Dự đoán {i + 1}", font=("Helvetica", 10), bg="white")
    percent_desc_label.grid(row=2 + i, column=3, padx=5)  # Mô tả cho các dự đoán
    bars.append(bar)
    labels.append(label)
    percent_labels.append(percent_label)
    percent_desc_labels.append(percent_desc_label)

# Thêm Label thông báo "Chưa vẽ ký tự"
info_label = tk.Label(root, text="Chưa vẽ ký tự", font=("Helvetica", 12), fg="red", bg="white")
info_label.place(x=50, y=CANVAS_SIZE + 50)

# Hàm xử lý ảnh và dự đoán
def predict():
    # Kiểm tra nếu canvas chưa vẽ gì
    if not canvas.find_all():
        info_label.config(text="Chưa vẽ ký tự", fg="red")  # Hiển thị thông báo "Chưa vẽ ký tự"
        return  # Dừng hàm nếu chưa vẽ ký tự

    # Cập nhật thông báo khi đã nhấn Submit
    info_label.config(text="Đang xử lý...", fg="blue")  # Hiển thị thông báo "Đang xử lý..."

    start_time = time.time()
    img = image.resize((IMG_SIZE, IMG_SIZE))
    img = ImageOps.invert(img)
    img_array = np.array(img).astype("float32") / 255.0
    img_array = img_array.reshape(1, IMG_SIZE, IMG_SIZE, 1)

    pred = model.predict(img_array)[0]
    top3 = np.argsort(pred)[-3:][::-1]

    # Hiển thị ảnh đã xử lý
    img_zoom = img.resize((CANVAS_SIZE, CANVAS_SIZE), Image.NEAREST)
    img_tk = ImageTk.PhotoImage(img_zoom)
    processed_label.config(image=img_tk)
    processed_label.image = img_tk

    # Hiển thị kết quả
    pred_label.config(text=CLASSES[top3[0]])
    for i, idx in enumerate(top3):
        labels[i].config(text=CLASSES[idx])
        bars[i].config(value=pred[idx] * 100)
        percent_labels[i].config(text=f"{pred[idx] * 100:.2f}%")  # Hiển thị phần trăm
        percent_desc_labels[i].config(text=f"Dự đoán {i + 1}")  # Thêm dòng mô tả

    info_label.config(text="Dự đoán", fg="green")  # Cập nhật thông báo khi dự đoán xong

# Hàm xóa
def clear():
    canvas.delete("all")
    draw.rectangle([0, 0, CANVAS_SIZE, CANVAS_SIZE], fill="white")
    processed_label.config(image="")
    pred_label.config(text="")
    for bar, label, percent_label, percent_desc_label in zip(bars, labels, percent_labels, percent_desc_labels):
        bar.config(value=0)
        label.config(text="")
        percent_label.config(text="0%")
        percent_desc_label.config(text="")
    info_label.config(text="Chưa vẽ ký tự", fg="red")  # Hiển thị lại thông báo khi xóa

# Nút
ttk.Button(root, text="Clear", command=clear).place(x=200, y=340, width=100, height=30)
ttk.Button(root, text="Submit", command=predict).place(x=360, y=340, width=100, height=30)

root.mainloop()

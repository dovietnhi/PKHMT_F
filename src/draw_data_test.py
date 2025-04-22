import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw
import os

# Đường dẫn thư mục dataset
dataset_dir = "chars_dataset"

# Danh sách ký tự
chars = [
    'a','b','c', 'd',
    'e', 'f', 'g', 'h', 
    'i', 'j','k', 'l', 
    'm', 'n','o','p', 
    'q', 'r', 's', 't',
    'u','v', 'w', 'x', 
    'y', 'z', '0', '1', 
    '2', '3', '4', '5', 
    '6', '7', '8', '9'
]


# Kích thước ảnh
image_size = 28

# Tạo thư mục lưu dữ liệu nếu chưa có
os.makedirs(dataset_dir, exist_ok=True)
for char in chars:
    os.makedirs(os.path.join(dataset_dir, char), exist_ok=True)

class DrawApp:
    def __init__(self, master):
        self.master = master
        master.title("Vẽ ký tự tiếng Việt")

        # Canvas
        self.canvas = tk.Canvas(master, width=200, height=200, bg='white')
        self.canvas.pack()

        # PIL image để lưu lại nét vẽ
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.start)

        # Dropdown chọn ký tự
        self.selected_char = tk.StringVar()
        self.char_menu = ttk.Combobox(master, textvariable=self.selected_char, values=chars)
        self.char_menu.set(chars[0])
        self.char_menu.pack(pady=5)

        # Nút lưu
        self.save_button = tk.Button(master, text="Lưu", command=self.save)
        self.save_button.pack()

        # Nút xóa
        self.clear_button = tk.Button(master, text="Xóa", command=self.clear)
        self.clear_button.pack()

    def start(self, event):
        self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.last_x, self.last_y, x, y, width=8, fill='black', capstyle=tk.ROUND, smooth=True)
        self.draw.line([self.last_x, self.last_y, x, y], fill='black', width=8)
        self.last_x, self.last_y = x, y

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), "white")
        self.draw = ImageDraw.Draw(self.image)

    def save(self):
        char = self.selected_char.get()
        if not char:
            print("Chưa chọn ký tự!")
            return
        save_dir = os.path.join(dataset_dir, char)
        os.makedirs(save_dir, exist_ok=True)
        count = len(os.listdir(save_dir)) + 1
        filename = f"{char}_{count:03d}.png"
        save_path = os.path.join(save_dir, filename)

        # Resize về chuẩn (28x28)
        resized_image = self.image.resize((image_size, image_size))
        resized_image.save(save_path)
        print(f"✅ Đã lưu: {save_path}")
        self.clear()

# Chạy app
root = tk.Tk()
app = DrawApp(root)
root.mainloop()
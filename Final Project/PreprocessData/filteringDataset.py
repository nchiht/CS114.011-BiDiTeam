import os
import re

# Xóa những dòng không có label trong label.txt
def filter_lines_without_suffix(label_file, suffixes_to_keep):
    try:
        # Đọc nội dung từ file label
        with open(label_file, 'r', encoding="utf8") as file:
            lines = file.readlines()

        # Lọc những dòng có hậu tố trong danh sách
        filtered_lines = [line for line in lines if any(suffix in line for suffix in suffixes_to_keep)]

        # Xóa file cũ
        tmp_label_file = label_file
        os.remove(label_file)

        # Ghi nội dung đã lọc vào file mới
        with open(tmp_label_file, 'w', encoding="utf-8") as file:
            file.writelines(filtered_lines)

        print("Đã lọc và ghi vào file mới.")

    except FileNotFoundError:
        print(f"File {label_file} không tồn tại.")

# Thay đổi 'duong_dan_label_file' thành đường dẫn thực tế của file label.txt
duong_dan_label_file = './OCR_data/train_label.txt'
# duong_dan_label_file = './OCR_data/test_label.txt'
# duong_dan_label_file = './OCR_data/val_label.txt'


# Hậu tố cần giữ lại
suffixes_to_keep = [f'/{a}/{b}' for a in ['other', 'title', 'author', 'publisher'] for b in range(31)]

# Gọi hàm để lọc dòng có hậu tố không nằm trong danh sách
filter_lines_without_suffix(duong_dan_label_file, suffixes_to_keep)


# Xóa những ảnh không xuất hiện trong file label
def filter_images_from_label_file(image_folder, label_file):
    # Đọc danh sách đường dẫn hình ảnh từ label file
    with open(label_file, 'r', encoding="utf-8") as label_file:
        image_paths = ['./' + line.split()[0] for line in label_file.readlines()]

    # Lấy danh sách tất cả các tệp tin trong thư mục hình ảnh
    all_images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

    # Lọc danh sách hình ảnh không có trong danh sách từ label file
    # images_to_keep = list(filter(lambda x: os.path.join(image_folder, x) in image_paths, all_images))
    images_to_keep = [img.split('/')[2] for img in image_paths]

    # Xóa những tệp tin không có trong danh sách từ label file
    for image in all_images:
        if image not in images_to_keep:
            os.remove(os.path.join(image_folder, image))
            print(f"Đã xóa: {os.path.join(image_folder, image)}")

# # Thay đổi 'duong_dan_thu_muc_hinh_anh' và 'duong_dan_label_file' thành đường dẫn thực tế của thư mục hình ảnh và file label.txt
duong_dan_thu_muc_hinh_anh = './OCR_data/train_images'
# duong_dan_thu_muc_hinh_anh = './OCR_data/test_images'
# duong_dan_thu_muc_hinh_anh = './OCR_data/val_images'

# # Gọi hàm để xóa ảnh không có trong label file
filter_images_from_label_file(duong_dan_thu_muc_hinh_anh, duong_dan_label_file)
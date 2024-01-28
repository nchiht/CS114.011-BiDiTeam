import random

def shuffle_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    random.shuffle(lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# Đường dẫn đến file cần xáo trộn
file_path = './OCR_data/train_label.txt'

# Gọi hàm để xáo trộn các dòng trong file
shuffle_lines(file_path)

import os
import random
import shutil

def split_data(input_folder, output_folder, ratios):
    assert sum(ratios) == 1.0, "Tổng tỷ lệ phải bằng 1"

    # Tạo thư mục test và val nếu chưa tồn tại
    test_folder = os.path.join(output_folder, 'test')
    val_folder = os.path.join(output_folder, 'val')
    
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)

    # Đọc danh sách tất cả các ảnh và label từ file train_label.txt
    with open(os.path.join(input_folder, 'train_label.txt'), 'r') as label_file:
        labels = label_file.readlines()

    # Lấy số lượng ảnh và label
    num_samples = len(labels)

    # Tính số lượng ảnh cần chia vào mỗi thư mục
    num_test = int(ratios[0] * num_samples)
    num_val = int(ratios[1] * num_samples)

    # Tạo danh sách các chỉ số của ảnh để chia
    indices = list(range(num_samples))
    random.shuffle(indices)

    # Chia ảnh vào thư mục test
    test_indices = indices[:num_test]
    for idx in test_indices:
        image_path = os.path.join(input_folder, 'train_images', f'image{idx + 1}.jpg')
        shutil.move(image_path, os.path.join(test_folder, f'image{idx + 1}.jpg'))
        with open(os.path.join(test_folder, 'test_label.txt'), 'a') as test_label_file:
            test_label_file.write(labels[idx])

    # Chia ảnh vào thư mục val
    val_indices = indices[num_test:num_test + num_val]
    for idx in val_indices:
        image_path = os.path.join(input_folder, 'train_images', f'image{idx + 1}.jpg')
        shutil.move(image_path, os.path.join(val_folder, f'image{idx + 1}.jpg'))
        with open(os.path.join(val_folder, 'val_label.txt'), 'a') as val_label_file:
            val_label_file.write(labels[idx])

    print(f"Chia dữ liệu thành công. {num_test} ảnh vào thư mục test và {num_val} ảnh vào thư mục val.")

# Đặt đường dẫn thư mục đầu vào và đầu ra
input_folder = '/path/to/your/dataset'
output_folder = '/path/to/your/output/folder'

# Đặt tỷ lệ phân phối
ratios = [0.7, 0.15]

# Thực hiện chia tỷ lệ dữ liệu
split_data(input_folder, output_folder, ratios)

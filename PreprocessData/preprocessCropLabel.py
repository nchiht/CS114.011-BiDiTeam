filePath = './crop_images/train_crop_imgs.txt'
# filePath = './crop_images/test_crop_imgs.txt'
# filePath = './crop_images/val_crop_imgs.txt'

outputPath = './crop_images/train_crop_imgs.txt'
# outputPath = './crop_images/test_crop_imgs.txt'
# outputPath = './crop_images/val_crop_imgs.txt'

# Đọc nội dung từ file
with open(filePath, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Loại bỏ hai đoạn cuối cùng của mỗi dòng sau dấu "/"
modified_lines = ["/".join(line.split("/")[:-2]) + '\n' for line in lines]

# Ghi nội dung đã chỉnh sửa vào file mới
with open(outputPath, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)
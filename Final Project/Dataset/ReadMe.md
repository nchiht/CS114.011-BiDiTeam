# Thông tin bộ dữ liệu: 
- Số lượng ảnh: 964 ảnh
- Định dạng ảnh: Đuôi .jpg, .JPG
- Kích thước ảnh: 961 x 1280
- Các ảnh được chụp chính diện, rõ ràng các văn bản có trên bìa sách.
- Bộ dữ liệu được lưu trữ trên nền tảng Kaggle: ***https://www.kaggle.com/datasets/chithinguyen/vietnamese-book-covers***
# Train - Validation - Test
- Bộ dữ liệu được chia ra thành 3 tập train, val và test một cách ngẫu nhiên theo tỉ lệ train:val:test = 7:1,5:1,5
- Tập train: 700 ảnh 
- Tập val: 132 ảnh
- Tập test: 132 ảnh
# Sơ đồ phân bố dữ liệu
```
├── OCR_data/
│ ├── test_images/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ ├── train_images/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ ├── val_images/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ ├── test_label.txt
│ ├── train_label.txt
│ └── val_label.txt
│ 
├── YOLO_data/
│ ├── test_images/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ ├── train_images/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ ├── val_images/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ └── data.yaml
│ 
├── crop_images/
│ ├── crop_img/
│ │ ├── image0.jpg
│ │ ├── image1.jpg
│ │ └── ...
│ ├── test_crop_imgs.txt
│ ├── train_crop_imgs.txt
│ └── val_crop_imgs.txt
│ 
```
# Giải thích sơ đồ cây dữ liệu:
- Bộ dữ liệu gốc nằm ở thư mục OCR_data. Trong quá trình thực hiện phát sinh ra các vấn đề về định dạng dữ liệu dành cho Yolo và VietOCR nên đã được định dạng lại thích hợp hơn. Cụ thể là định dạng dành cho Yolo ở thư mục **YOLO_data** và VietOCR ở thư mục **crop_images**

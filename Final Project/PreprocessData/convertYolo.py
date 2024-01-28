import cv2
import math

def convert_to_yolo_format(annotation_file, label_mapping):
    with open(annotation_file, 'r', encoding='utf-8') as file:
        annotation_data = file.readlines()

    yolo_annotations = []

    for entry in annotation_data:
        image_path, objects = entry.split('\t')
        print(image_path)
        false = False
        true = True
        objects = eval(objects)
        # print(objects)

        # Get image dimensions dynamically
        image = cv2.imread(image_path.strip())
        if((image is not None)):
          height, width, _ = image.shape

          yolo_annotation = []
          for obj in objects:
              label = obj['transcription'].split('/')[1]
              if label in label_mapping:
                  label_id = label_mapping[label]
                  x_center = (obj['points'][0][0] + obj['points'][2][0]) / (2.0 * width)
                  y_center = (obj['points'][0][1] + obj['points'][2][1]) / (2.0 * height)
                  w = abs(obj['points'][2][0] - obj['points'][0][0]) / width
                  h = abs(obj['points'][2][1] - obj['points'][0][1]) / height

                  yolo_annotation.append(f"{label_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}")
          with open('./YOLO_data/' + image_path.split('.')[0] + '.txt', 'w') as f:
              for line in yolo_annotation:
                f.write("%s\n" % line)
          if yolo_annotation:
              yolo_annotations.append(f"{image_path.strip()} {' '.join(yolo_annotation)}")

    return yolo_annotations

# Define your label mapping
label_mapping = {'other': 0, 'author': 1, 'title': 2, 'publisher': 3}

# Replace 'annotation.txt' with the path to your annotation file
annotation_file_path = './OCR_data/train_label.txt'
# annotation_file_path = './OCR_data/val_label.txt'
# annotation_file_path = './OCR_data/test_label.txt'


yolo_formatted_annotations = convert_to_yolo_format(annotation_file_path, label_mapping)

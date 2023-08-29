import json
import cv2
import numpy as np

with open('submission.json', "r") as f:
    json_data = json.load(f)

a = []
for item in json_data:
    if item['image_id'] == 0 and item['category_id'] == 11:
        a.append(item['bbox'])

image = cv2.imread('../split_data/datasets/DelftBikes/test/images/48682.jpg')
for i in range(len(a)):
    x, y, w, h = int(a[i][0]), int(a[i][1]), int(a[i][2]), int(a[i][3])
    color = list(np.random.random(size=3) * 256)
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
    cv2.imshow('Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

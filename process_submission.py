import os
import json

folder_path = "../split_data/datasets/DelftBikes/test/images/"
image_files = sorted([os.path.splitext(f)[0] for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

json_file_path = "submission.json"
with open(json_file_path, "r") as f:
    json_data = json.load(f)
json_data.sort(key=lambda x: str(x["image_id"]))

image_mapping = {image_file: i for i, image_file in enumerate(image_files)}

a = []
for item in json_data:
    image_id = str(item["image_id"])
    numeric_id = image_mapping.get(image_id)
    if numeric_id:
        item["image_id"] = numeric_id
    if item['image_id'] == 48682:
        item['image_id'] = 0
    #item['category_id'] += 1

with open(json_file_path, "w") as f:
    json.dump(json_data, f)

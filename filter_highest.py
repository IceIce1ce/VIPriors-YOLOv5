import json

with open('submission.json', 'r') as json_file:
    data = json.load(json_file)

highest_scores = {}

for entry in data:
    image_id = entry['image_id']
    category_id = entry['category_id']
    score = entry['score']
    if image_id in highest_scores:
        if category_id in highest_scores[image_id]:
            if score > highest_scores[image_id][category_id]['score']:
                highest_scores[image_id][category_id] = {'bbox': entry['bbox'], 'score': score}
        else:
            highest_scores[image_id][category_id] = {'bbox': entry['bbox'], 'score': score}
    else:
        highest_scores[image_id] = {category_id: {'bbox': entry['bbox'], 'score': score}}

result = []
for image_id, categories in highest_scores.items():
    for category_id, data in categories.items():
        result.append({
            'image_id': image_id,
            'category_id': category_id,
            'bbox': data['bbox'],
            'score': data['score']
        })

with open('result.json', 'w') as json_output:
    json.dump(result, json_output)
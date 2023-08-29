import glob
import shutil

list_images = sorted(glob.glob('train/images/*.jpg'))
list_annotations = sorted(glob.glob('train/annotations/*.txt'))
list_labels = sorted(glob.glob('train/labels/*.txt'))

for i in range(1500):
	shutil.move(list_images[i], "train4/images")
	shutil.move(list_annotations[i], "train4/annotations")
	shutil.move(list_labels[i], "train4/labels")

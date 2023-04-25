import cv2
import os
from tqdm import tqdm 
path = 'data/new_augmented_data/images'

for img_name in tqdm(os.listdir(path)):
    img = cv2.imread(path+'/'+img_name)
    resized_img = cv2.resize(img, (640, 640))
    cv2.imwrite(f'data/resized_images/{img_name}', resized_img)

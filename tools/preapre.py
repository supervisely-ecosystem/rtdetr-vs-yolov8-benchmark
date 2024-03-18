import supervisely as sly
import os
import cv2

input_dir = "benchmark"

for file in os.listdir(input_dir):
    if os.path.isdir(f"{input_dir}/{file}"):
        continue
    img = sly.image.read(f"{input_dir}/{file}")
    img = cv2.resize(img, (640, 640), interpolation=cv2.INTER_LINEAR)
    sly.image.write(f"{input_dir}/x640/{file}", img)
    

# now resize to 1280x1280
for file in os.listdir(input_dir):
    if os.path.isdir(f"{input_dir}/{file}"):
        continue
    img = sly.image.read(f"{input_dir}/{file}")
    img = cv2.resize(img, (1280, 1280), interpolation=cv2.INTER_LINEAR)
    sly.image.write(f"{input_dir}/x1280/{file}", img)
    
    
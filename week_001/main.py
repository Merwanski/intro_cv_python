# import necessary packages 
import numpy as np
import cv2

# path to image
path_to_image = "data/cv_image_000.jpg"
# read the image with cv2
image = cv2.imread(path_to_image)

print('Original Dimensions : ', image.shape)

scale_percent = 60 # percent of original size
width  = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# resize the image
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ', resized.shape)

# show the image
cv2.imshow("Original image", image)
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()










data_to_video = "data/bee_farm.mp4"
cap = cv2.VideoCapture(data_to_video)

while True:
    res, frame = cap.read()
    if res:
        cv2.imshow("image", frame)
        cv2.waitKey(10)
    else:
        break





cap.release()

# import the necessary packages
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
# load the image

#Resize the image
img1 = Image.open(args["image"])
new_width  = 600
new_height = 400
img1 = img1.resize((new_width, new_height), Image.ANTIALIAS)
img1.save(args["image"])

img = cv2.imread(args["image"])

# Convert BGR to HSV

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of black color in HSV

lower_val = np.array([0,0,0])

upper_val = np.array([105,105,105])

# Threshold the HSV image to get only black colors

mask = cv2.inRange(hsv, lower_val, upper_val)

# Bitwise-AND mask and original image

res = cv2.bitwise_and(img,img, mask= mask)

# invert the mask to get black letters on white background

res2 = cv2.bitwise_not(mask)

# display image

#Check Fire

check_if_fire_detected = cv2.countNonZero(mask)
print(check_if_fire_detected)
if int(check_if_fire_detected) >= 20000 :
    print('***************Fire Detected*********************')
    
# images = []
# images.append(img)
# images.append(res2)

# create figure
# fig = plt.figure(figsize=(10, 7))
#   
# # setting values to rows and column variables
# rows = 2
# columns = 2
# 
# # Adds a subplot at the 1st position
# fig.add_subplot(rows, columns, 1)
  
# showing image
# plt.imshow(img)
# plt.axis('off')
# plt.title("First")
  
# Adds a subplot at the 2nd position
#fig.add_subplot(rows, columns, 2)
  
# showing image
# plt.imshow(res2)
# plt.axis('off')
# plt.title("Second")


# cv2.imshow("images",images[1])
# 
cv2.imshow("img",img)

cv2.imshow("img2", res2)

cv2.waitKey(0)

cv2.destroyAllWindows()
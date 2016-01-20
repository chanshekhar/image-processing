import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dip.jpg',1)
edges = cv2.Canny(img,100,200) # Canny is a inbuilt function for finding edges by using threshold values (image, thres1 ,thres2)

plt.subplot(121),plt.imshow(img) # ploting as subplot & positioning the image in 1 row 2 coloumns 1st image
plt.title('Original Image'), plt.xticks([]), plt.yticks([]) # writing title on the displayed image  & Set X & Y Limits of the current image title location
plt.subplot(122),plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show() # displaying the Plot 
cv2.waitKey(0)










    

import cv2
import numpy as np
import sys

INPUT_DIR = sys.argv[1]

img = cv2.imread(INPUT_DIR,0)
IMG_WIDTH = img.shape[0]
IMG_HEIGHT = img.shape[1]

cv2.imshow('image',img)
cv2.waitKey(0)
def f(w1,w2,w3,w4):
    for i in range(IMG_WIDTH):
        for j in range(IMG_HEIGHT):
            error_val = 0
            if img.item(i,j)>128:
                error_val = img.item(i,j)-255
                img.itemset(i,j,255)
            else:
                error_val = img.item(i,j)
                img.itemset(i,j,0)
            if i<IMG_WIDTH-1: #south
                img.itemset(i+1,j,(img.item(i+1,j)+((w1)*error_val)))
            if j>0 : #east
                img.itemset(i,j-1,(img.item(i,j-1)+((w2)*error_val)))
            if j>0 and i<IMG_WIDTH-1: #south east
                img.itemset(i+1,j-1,(img.item(i+1,j-1)+((w3)*error_val)))
            if j<IMG_HEIGHT-1 and i<IMG_WIDTH-1: #south west
                img.itemset(i+1,j+1,(img.item(i+1,j+1)+((w4)*error_val)))
    cv2.imshow('image',img)
    cv2.waitKey(0)



f(5/16,7/16,1/16,3/16)
# f(4/16,4/16,4/16,4/16)

# for i in range(7):
#     for j in range(i+1,7):
#         for k in range(j+1,7):
#             t = 16-i-j-k
#             if t>0:
#                 f(i/16,j/16,k/16,t/16)


# import cv2
# import numpy as np

# INPUT_DIR = "Q1.jpg"
# img = cv2.imread(INPUT_DIR,0)
# IMG_WIDTH = img.shape[0]
# IMG_HEIGHT = img.shape[1]

# cv2.imshow('image',img)
# cv2.waitKey(0)

# for i in range(IMG_WIDTH):
#     for j in range(IMG_HEIGHT):
#         error_val = 0
#         if img.item(i,j)>128:
#             error_val = img.item(i,j)-255
#             img.itemset(i,j,255)
#         else:
#             error_val = img.item(i,j)
#             img.itemset(i,j,0)
#         if i<IMG_WIDTH-1 and (img.item(i+1,j)+((5/16)*error_val))<255 : #south
#             img.itemset(i+1,j,(img.item(i+1,j)+((5/16)*error_val)))
#         if j>0 and (img.item(i,j-1)+((7/16)*error_val))<255: #east
#             img.itemset(i,j-1,(img.item(i,j-1)+((7/16)*error_val)))
#         if j>0 and i<IMG_WIDTH-1 and (img.item(i+1,j-1)+((1/16)*error_val))<255: #south east
#             img.itemset(i+1,j-1,(img.item(i+1,j-1)+((1/16)*error_val)))
#         if j<IMG_HEIGHT-1 and i<IMG_WIDTH-1 and (img.item(i+1,j+1)+((3/16)*error_val))<255: #south west
#             img.itemset(i+1,j+1,(img.item(i+1,j+1)+((3/16)*error_val)))
        

# cv2.imshow('image',img)
# cv2.waitKey(0)
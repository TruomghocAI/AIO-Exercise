import cv2 as cv
import numpy as np
 
cap = cv.VideoCapture(0)
while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    

 
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)
    new_img_3d1 = cv.merge([mask_blue, mask_blue, mask_blue])
    xanh = np.uint8([[[255,0,0]]])
    blue_img = np.where(new_img_3d1 == 255, xanh, 0)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask_blue)
    cv.imshow('blue_img',blue_img)
    
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])    
    mask_red = cv.inRange(hsv, lower_red, upper_red)
    new_img_3d2 = cv.merge([mask_red, mask_red, mask_red])
    do = np.uint8([[[0,0,255]]])
    red_img = np.where(new_img_3d2 == 255, do, 0)
    cv.imshow('mask',mask_red)
    cv.imshow('red_img',red_img)
    
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    mask_green = cv.inRange(hsv, lower_green, upper_green)
    new_img_3d3 = cv.merge([mask_green, mask_green, mask_green])
    lacay = np.uint8([[[0,255,0]]])
    green_img = np.where(new_img_3d3 == 255, lacay, 0)
    cv.imshow('mask',mask_green)
    cv.imshow('green_img',green_img)
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv.destroyAllWindows()
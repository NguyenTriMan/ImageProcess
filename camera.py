import urllib
import cv2
import numpy as np


url = 'http://192.168.43.200:4747/video'

cap = cv2.VideoCapture(url)

while True:
  ret, frame = cap.read()
  cv2.imshow('Image', frame)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):  #push 'q' to exit 
    cv2.imwrite('C:/Users/Admin/Documents/pythonVisualcode/image.jpg',frame) #print image 
    break
     

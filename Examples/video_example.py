'''
Code taken from https://python.plainenglish.io/working-with-images-and-videos-in-opencv-and-python-9ec6eec4dbf5

adapted file system saving destination a tad with os

'''

import cv2
import numpy as np
import os

### FILE SAVING ###
f_name = 'output.avi' # change this value here ulitmately could make it a command line arg
save_path = os.path.join(os.path.dirname(os.getcwd()), 'Media', f_name)

### VIDEO CREATION ###
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(save_path, fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('video feed', frame)
    cv2.imshow('gray feed', gray)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

### SAFE EOP ###
cap.release()
out.release()
cv2.destroyAllWindows()


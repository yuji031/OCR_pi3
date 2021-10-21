import cv2
import os
from PIL import Image, ImageFont, ImageDraw
import pyocr
import numpy as np




def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    x = width//3
    y = height//5

    w = width//4
    h = height//6

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    
    while True:
        ret, frame = cap.read()

        cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255),thickness= 4)

        frame_2 = cv2.flip(frame, 1)

        cv2.imshow(window_name, frame_2)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite('{}.{}'.format(base_path, ext), frame)
            
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'data/temp', 'camera_capture')

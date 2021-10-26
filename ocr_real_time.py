from PIL import Image
import cv2
import sys 
import pyocr
import pyocr.builders
import time

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

langs = tool.get_available_languages()
lang = langs[0]
cap = cv2.VideoCapture(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width//3
y = height//5

w = width//3
h = height//8

last_txt = ""

while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0,0,255), thickness=4)

    area = (220,101, 424,164)

    txt = tool.image_to_string(
        Image.fromarray(frame).crop(area),
        lang = "eng",
        builder = pyocr.builders.TextBuilder(tesseract_layout=6) 
    )


    if len(txt) !=0 and txt != last_txt:
        if txt.isdecimal():
            last_txt = txt
            print(txt)

    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

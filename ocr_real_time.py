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
last_txt = ""
while True:
    ret, frame = cap.read()
    
    txt = tool.image_to_string(
        Image.fromarray(frame),
        lang = "eng",
        builder = pyocr.builders.TextBuilder(tesseract_layout=6) 
    )


    if len(txt) !=0 and txt != last_txt:
        last_txt = txt
        print(txt)

    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

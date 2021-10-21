from PIL import Image, ImageFont, ImageDraw
import pyocr
import numpy as np


tools = pyocr.get_available_tools()
tool = tools[0]

area = (217,100, 367,170)

txt = tool.image_to_string(
    Image.open('data/temp/camera_capture.jpg').crop(area),
    lang = "eng",
    builder=pyocr.builders.TextBuilder()
    )

print(txt)
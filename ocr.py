from PIL import Image
import pyocr
import numpy

tools = pyocr.get_available_tools()
tool = tools[0]

area = (218,97, 425,151)

imgj = Image.open('C:\\programming\\SSH_programm\\data\\temp\\camera_capture.jpg')
txt = tool.image_to_string(
    img.crop(area),
    lang = "eng",
    builder = pyocr.builders.TextBuilder()
    )

print(txt)

from PIL import Image
from pytesseract import pytesseract


def extract_text(img):
    img = Image.open(img)
    text = pytesseract.image_to_string(img)
    return text


# TODO
# 1. pytesseract.tesseract_cmd = settings.TESSERACT_PATH

# 2. if content_type == "image":
# elif content_type == "pdf":
#     import pymupdf

#     pdf = await file.download_as_bytearray()
#     pdf = pymupdf.open(stream=pdf)
#     text = ""
#     for page in pdf:
#         text += page.getText()
# else:
#     text = "Unsupported file type"

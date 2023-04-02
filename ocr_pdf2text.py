# from PIL import Image
# import pytesseract
# import sys
# from pdf2image import convert_from_path
# from db_config import config
#
#
# try:
#     image_counter = 1
#
#     # PDF_file = 'lg.pdf'
#     # pages = convert_from_path(PDF_file)
#     #
#     # for page in pages:
#     #     filename = "page_" + str(image_counter) + ".jpg"
#     #     filepath = config.img_path + filename
#     #     page.save(filepath, 'JPEG')
#     #     image_counter = image_counter + 1
#     #
#     # filelimit = image_counter
#     # outfile = "out_text.txt"
#     # f = open(outfile, "a")
#     # for i in range(1, filelimit):
#     #     filename = "page_" + str(i) + ".jpg"
#     #     filepath = config.img_path + filename
#     #     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     #     text = str(((pytesseract.image_to_string(Image.open(filepath)))))
#     #     f.write(text)
#     # f.close()
#
#     filename = "D:\Python-Priti\Tools\pdf_to_csv\page_2.jpg"
#     # filepath = config.img_path + filename
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     text = str(((pytesseract.image_to_string(Image.open(filename)))))
#     print(text)
#
# except Exception as e:
#     print(e)

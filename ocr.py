from wand.image import Image as Img
from PIL import Image
import pytesseract
import os
import sys

def pdf2jpg(file):
	with Img(filename=file, resolution=300) as img:
		img.compression_quality = 99
		img.save(filename=os.path.splitext(file)[0] + '.jpg')

def jpg2text(file):
	text = pytesseract.image_to_string(Image.open(os.path.splitext(file)[0]+'.jpg'))
	print(text)

def main(file):
	if(file.endswith('.pdf')):
		pdf2jpg(file)

	jpg2text(file)


if __name__ == "__main__":
	main('scan.jpg')
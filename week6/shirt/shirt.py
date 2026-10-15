import sys
import csv
import os
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
	sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")

in_end, out_end = os.path.splitext(sys.argv[1])[1].lower(), os.path.splitext(sys.argv[2])[1].lower()
path_list = [".jpg", ".jpeg", ".png"]
if in_end not in path_list:
	sys.exit("Invalid input")
elif out_end not in path_list:
	sys.exit("Invalid output")

if (in_end != out_end):
	sys.exit("Input and output have different extensions")
try:
	pic = Image.open(sys.argv[1])
	shirt = Image.open("shirt.png")
	size = shirt.size
	cropped_image = ImageOps.fit(pic, size)
	cropped_image.paste(shirt , shirt)
	cropped_image.save(sys.argv[2])

except FileNotFoundError:
	sys.exit("Input does not exist")
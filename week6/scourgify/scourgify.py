import sys
import csv

if len(sys.argv) < 3:
	sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")

try:
	with open(sys.argv[1], "r") as file:
		student_list = []
		reader = csv.DictReader(file)
		for row in reader:
			student_list.append(row)
	with open(sys.argv[2], "w") as new_file:
		field_names = ["first", "last", "house"]
		writer = csv.DictWriter(new_file, fieldnames = field_names)
		writer.writeheader()
		for dicts in student_list:
			name, house = dicts["name"], dicts["house"]
			last, first = name.split(', ')
			writer.writerow({"first": first, "last": last, "house": house})
except FileNotFoundError:
	sys.exit(f"Could not read {sys.argv[1]}")

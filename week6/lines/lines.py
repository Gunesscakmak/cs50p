import sys

argno = len(sys.argv)
if argno != 2:
	amount = "many"
	if argno < 2:
		amount = "few"
	sys.exit(f"Too {amount} command-line arguments") 
try:
	if sys.argv[1].endswith('.py'):
		with open(sys.argv[1], "r") as file:
			lines = file.readlines()
			counter = 0
			for line in lines:
				if line.lstrip() == "" or line.lstrip().startswith('#'):
					pass
				else:
					counter += 1
		print(counter)
	else:
		sys.exit("Not a Python file")
except FileNotFoundError:
	sys.exit("File does not exist")

#not: try blogunu, hata firlatmasini bekledigin satirlarla sinirli tut.
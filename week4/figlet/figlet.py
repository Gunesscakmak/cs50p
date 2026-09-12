import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
font_list = figlet.getFonts()
if len(sys.argv) == 1:
    f = font_list[random.randint(0, len(font_list)-1)]
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
        f = sys.argv[2] 
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")

x = input("Input: ")
figlet.setFont(font=f)
print(f"Output: \n\n{figlet.renderText(x)}")
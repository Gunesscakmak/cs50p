import inflect

p = inflect.engine()
x_list = []
while True:
    try:
        x = input("Name: ")
        x_list.append(x)
    except (EOFError):
        break

print(f"Adieu, adieu, to {p.join(x_list, conj = "and")}")

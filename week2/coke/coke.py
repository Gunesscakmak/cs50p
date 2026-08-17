
remain = 50
while (remain > 0):
    print(f"Amount Due: {remain}")
    user = int(input("Insert Coin: "))
    if user == 25 or user == 10 or user == 5:
        remain = remain - user
print(f"Change Owed: {abs(remain)}")  
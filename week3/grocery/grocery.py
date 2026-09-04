grocery_dict = {}
counter = 0
while True:
    try:
        item = input().upper()
        if item in grocery_dict:
            grocery_dict[item]+=1
        else:
            counter+=1
            grocery_dict[item] = counter
        counter = 0
    except EOFError:
        break
print("\n")
for key,val in sorted(grocery_dict.items()):
    print(val, key)
  



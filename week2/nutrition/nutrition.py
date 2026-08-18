
x = input("Item: ").lower()

fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "sweet cherries" : 100
}

if x in fruits:
    print(f"Calories: {fruits.get(x)}")
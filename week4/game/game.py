import random 

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        rand = random.randint(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess <= 0:
                    pass
                elif (guess < rand):
                    print("Too small!")
                    pass
                elif (guess > rand):
                    print("Too large!")
                    pass
                else:
                    print("Just right!")
                    break
            except ValueError:
                pass
        break
    except ValueError:
        pass

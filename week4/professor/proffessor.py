from random import randint
def main():
    level = get_level()
    score = 0
    for i in range(10):
        first_int = generate_integer(level)
        second_int = generate_integer(level)
        flag = 1
        while True:
            try:
                answer = int(input(f"{first_int} + {second_int} = "))
                if answer != first_int + second_int:    
                    if flag < 3:
                            print("EEE")
                            flag += 1
                            raise ValueError
                    else:    
                        print("EEE")
                        print(f"{first_int} + {second_int} = {first_int + second_int}")
                        break                        
                else:
                    score += 1
                    break
            except ValueError:
                pass
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                raise ValueError
            return (level)
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        rand_int = randint(0,9)
    elif level == 2:
        rand_int = randint(10,99)
    elif level == 3:
        rand_int = randint(100,999)
    else:
        raise ValueError
    return rand_int


if __name__ == "__main__":
    main()
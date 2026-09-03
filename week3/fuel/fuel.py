while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split('/') 
        x = int(x)
        y = int(y)
        if x < 0 or x > y:
            raise ValueError
        percentage = int(x/y * 100)
        if percentage >= 99:
            print("F")
        elif percentage <= 1:
            print("E") 
        else:
            print(f"{percentage}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
    


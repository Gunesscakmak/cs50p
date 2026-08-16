def main():
    x = input("What time is it? ").strip()
    a = convert(x)
    if (a <= 8 and a >= 7):
        print("breakfast time")
    elif (a <= 13 and a >= 12):
        print("lunch time")
    elif (a <= 19 and a >= 18):
        print("dinner time")


def convert(time):
    if (time.endswith('p.m.')):
        hr, min = time.removesuffix('p.m.').strip().split(":")
        min = float(float(min) / 60)
        hr = float(hr) + min + 12
    else:
        if (time.endswith('a.m.')):
            hr, min= time.removesuffix('a.m.').strip().split(':')
        else:
            hr, min = time.split(":")
        min = float(float(min) / 60)
        hr = float(hr) + min
    return (hr)

if __name__ == "__main__":
    main()
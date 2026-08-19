def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    for a in s:
        if not a.isalnum():
            return False
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0].isdecimal() or s[1].isdecimal():
        return False
    for i in range(len(s)):
        if s[i].isdecimal():
            if s[i] == '0':
                return False
            if not s[i:].isdigit():
                return False
            break

    return True
main()

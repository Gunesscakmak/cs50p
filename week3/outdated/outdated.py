month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try: 
        date = input("Date: ")
        if '/' in date:
            split_date = date.split('/')
            month, day, year = int(split_date[0]), int(split_date[1]), int(split_date[2])
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
            else:
                continue
        elif ',' in date:
            split_date = date.split(',')
            date, year = split_date[0], int(split_date[1].strip())
            date = date.split(' ')
            month, day = date[0], int(date[1])
            if month in month_list and 1 <= day <= 31:
                print(f"{year:04}-{month_list.index(month) + 1:02}-{day:02}")
                break
            else:
                continue
        else:
            continue
    except (ValueError, IndexError):
        pass



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
        if date.index('/'):
            split_date = date.split('/')
            month, day, year = int(split_date[0]), int(split_date[1]), split_date[2]
            if month > 12 or day > 31:
                raise ValueError
            else:
                print(f"{year}-{month:02}-{day:02}")
                break
        if date.index(','):
            split_sdate = date.split(',')
            date, syear = split_sdate[0], split_sdate[1]
            sday = int(date.pop())
            print("f{sday}\n")
            smonth = date
            print("f{smonth}\n")
            if month_list.index(smonth):
                if sday > 31:
                    raise ValueError
                else:
                    print(f"{syear}-{month_list.index(smonth):02}-{sday:02}")
                    break
        else:
            pass
    except (ValueError):
        pass



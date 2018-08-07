def is_leap_year(year):
    a = int(year)
    if a%4 == 0 and a%400 + a%100 == 0:
        return True
    elif a%4 == 0 and a%100 == 0 and a%400 != 0:
        return False
    elif a%4 == 0 and a%100 != 0 and a%400 != 0:
        return True
    else:
        return False


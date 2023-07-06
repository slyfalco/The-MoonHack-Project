
def dtime(n):
    full = (n[-32]+n[-31]+n[-30]+n[-29]+n[-28]+n[-27]+n[-26]+n[-25]+n[-24]+n[-23]+n[-22]+n[-21]+n[-20]+n[-19]+n[-18]+n[-17])
    day = int(full[-8]+full[-7])
    if day == 1:
        day = str(day)
        day = (day+"st")
    elif day == 2:
        day = str(day)
        day = (day+"nd")
    elif day == 3:
        day = str(day)
        day = (day+"rd")
    elif day == 21:
        day = str(day)
        day = (day+"st")
    elif day == 22:
        day = str(day)
        day = (day+"nd")
    elif day == 23:
        day = str(day)
        day = (day+"rd")
    elif day == 31:
        day = str(day)
        day = (day+"st")
    else:
        day = str(day)
        day = (day+"th")
    month = int(full[-11]+full[-10])
    if month == 1:
        month = str("January")
    elif month == 2:
        month = str("Febuary")
    elif month == 3:
        month = str("March")
    elif month == 4:
        month = str("April")
    elif month == 5:
        month = str("May")
    elif month == 6:
        month = str("June")
    elif month == 7:
        month = str("July")
    elif month == 8:
        month = str("August")
    elif month == 9:
        month = str("September")
    elif month == 10:
        month = str("October")
    elif month == 11:
        month = str("November")
    elif month == 12:
        month = str("December")
    hour = int(full[-5]+full[-4])
    minute = str(full[-2]+full[-1])
    if hour < 12:
        hour = str(hour)
        minute = str(minute+"AM")
    elif hour == 12:
        hour = str(hour)
        minute = str(minute+"PM")
    else:
        hour = str(hour-12)
        minute = str(minute+"PM")
    year = str(full[-16]+full[-15]+full[-14]+full[-13])
    globals()[mystr] = (day+" "+month+" "+year+" at "+hour+":"+minute)


hello = "2022-10-17 02:50:25.085744+00:00"
print(hello)
print()
mystr = "hello"
dtime(hello)
print(hello)



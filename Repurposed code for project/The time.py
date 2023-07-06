from datetime import datetime

def now():
  day = datetime.today().day
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

  month = datetime.today().month
  if month == 1:
    month = "January"
  elif month == 2:
    month = "Febuary"
  elif month == 3:
    month = "March"
  elif month == 4:
    month = "April"
  elif month == 5:
    month = "May"
  elif month == 6:
    month = "June"
  elif month == 7:
    month = "July"
  elif month == 8:
    month = "August"
  elif month == 9:
    month = "September"
  elif month == 10:
    month = "October"
  elif month == 11:
    month = "November"
  elif month == 12:
    month = "December"
  time1 = datetime.today().hour
  if time1 < 12:
    noon = "AM"
  elif time1 == 12:
    noon = "PM"
  else:
    time1 = (time1-12)
    noon = "PM"
  time1 = str(time1)
  time2 = str(datetime.today().minute)
  time = str(time1+":"+time2+noon)
  print(day, month, datetime.today().year, time)

now()

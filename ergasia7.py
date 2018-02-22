import datetime

d = datetime.date.today()


while(d.year < 2028):
    if(d.weekday() == 0 and d.day == 8):
        print d
    d += datetime.timedelta(1)
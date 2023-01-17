import  datetime
d = datetime.date(2016,7,24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.month)
print(tday.day)

# weekday() -> monday=0 and sunday=6
# isoweekday() -> monday=1 and sunday=7

print(tday.weekday())
print(tday.isoweekday())

tdelta= datetime.timedelta(days=7)
print(tday+tdelta)  # shows date from 7 days after

t=datetime.time(12,30,40,100000) # time 12 hrs 30 min 40 sec and microsec
print(t)

dt = datetime.datetime(2016, 7, 26, 12,30, 45, 100000)
print(dt)
print(dt.time())
print(dt.year)

tdelta=datetime.timedelta(hours=12)
print(dt+tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today) # current local time with no time zone
print(dt_now) # current local time with timezone
print(dt_utcnow) #utc time with no time zone


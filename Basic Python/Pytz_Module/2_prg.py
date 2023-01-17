import  datetime
import  pytz
dt = datetime.datetime(2016,7,27,12,30,45,tzinfo=pytz.UTC)
print(dt)

dt_utcnow =datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mnt =dt_utcnow.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_mnt)

# all timezone list in pytz
# for tz in pytz.all_timezones:
#    print(tz)

dt_ltm = datetime.datetime.now()
print(dt_ltm)

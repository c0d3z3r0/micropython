import utime

def lastSundayOfMonth(year, month):
    last_day_ts = utime.mktime((year, month + 1, 0, 0, 0, 0, 0, 0, -1))
    last_weekday = utime.localtime(last_day_ts)[6] + 1
    return last_day_ts - (last_weekday * 86400)

cur_year = utime.localtime()[0]
# dst start/end is at 01:00 UTC
DSTSTART = lastSundayOfMonth(cur_year, 3) + 3600
DSTEND   = lastSundayOfMonth(cur_year, 10) + 3600
TZ = 1  # UTC+1

def time():
    t = utime.time() + TZ
    if DSTSTART < t < DSTEND:
        t += 1
    return int(t)

def localtime(ts=None):
    if ts is None:
        ts = time()
    t = utime.localtime(ts)
    if DSTSTART < ts < DSTEND:
        t = t[:-1] + (1,)
    return t

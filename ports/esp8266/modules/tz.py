import utime

TZ = 1  # UTC+1

def lastSundayOfMonth(year, month):
    last_day_ts = utime.mktime((year, month + 1, 0, 0, 0, 0, 0, 0, -1))
    last_weekday = utime.localtime(last_day_ts)[6] + 1
    return last_day_ts - (last_weekday * 86400)

def isdst(ts):
    year = utime.localtime(ts)[0]
    dst_start = lastSundayOfMonth(year, 3) + 3600
    dst_end = lastSundayOfMonth(year, 10) + 3600
    return (dst_start < ts < dst_end)

def utcoffset(ts=None):
    if ts is None:
        ts = utime.time()
    offset = TZ * 3600
    if isdst(ts):
        offset += 3600
    return offset

def localtime(ts=None):
    if ts is None:
        ts = utime.time()
    dst = isdst(ts)
    ts += TZ * 3600
    if dst:
        ts += 3600
    t = utime.localtime(ts)[:8] + (int(dst),)
    return t

def mktime(lt):
    ts = utime.mktime(lt)
    ts -= TZ * 3600
    if lt[8] == 1:
        ts -= 3600
    return ts

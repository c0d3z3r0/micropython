# dummy/proxy tz module

import utime

from utime import mktime, localtime

TZ = 1  # UTC+1

def isdst(ts):
    return bool(utime.localtime(ts)[8])

def utcoffset(ts=None):
    if ts is None:
        ts = utime.time()
    offset = TZ * 3600
    if isdst(ts):
        offset += 3600
    return offset

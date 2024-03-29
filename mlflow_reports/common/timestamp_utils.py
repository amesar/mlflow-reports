import time


TS_FORMAT = "%Y-%m-%d %H:%M:%S"
ts_now_seconds = round(time.time())
ts_now_fmt_utc = time.strftime(TS_FORMAT, time.gmtime(ts_now_seconds))
ts_now_fmt_local = time.strftime(TS_FORMAT, time.localtime(ts_now_seconds))


def now(as_utc=True):
    if as_utc:
        return time.strftime(TS_FORMAT, time.gmtime(round(time.time())))
    else:
        return time.strftime(TS_FORMAT, time.localtime(round(time.time())))


def fmt_ts_millis(millis, as_utc=True):
    if not millis:
        return None
    return fmt_ts_seconds(round(millis/1000), as_utc)


def fmt_ts_seconds(seconds, as_utc=True):
    if not seconds:
        return None
    ts_format = "%Y-%m-%d %H:%M:%S"
    if as_utc:
        ts = time.gmtime(seconds)
    else:
        ts = time.localtime(seconds)
    return time.strftime(ts_format, ts)

from math import floor
from re import compile


RE = compile(r'^(?P<sg>[+-])?((?P<h>\d+)\:)?(?P<m>\d{1,2})\:(?P<s>\d{1,2})(\.(?P<ms>\d+)?)?$')  # noqa: E501


def totimestr(ms: int) -> str:
    if ms < 0:
        sg = '-'
        ms = -ms
    else:
        sg = ''
    h = floor(ms / 3600000)
    m = floor((ms % 3600000) / 60000)
    s = floor((ms % 60000) / 1000)
    if h == 0:
        return f"{sg}{m:02}:{s:02}.{ms%1000:03}"
    else:
        return f"{sg}{h}:{m:02}:{s:02}.{ms%1000:03}"


def parsetimestr(s: str) -> int:
    r = RE.search(s)
    if r is None:
        return int(s)
    else:
        d = r.groupdict()
        r = 0
        if d['h']:
            r += int(d['h']) * 3600000
        r += int(d['m']) * 60000
        r += int(d['s']) * 1000
        if d['ms']:
            r += round(int(d['ms']) * (10 ** (3 - len(d['ms']))))
        return -r if d['sg'] == '-' else r

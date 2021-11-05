from typing import IO
from math import ceil


def readbyte(f: IO[bytes]) -> int:
    return f.read(1)[0]


def readint(f: IO[bytes]) -> int:
    return int.from_bytes(f.read(4), 'little', signed=True)


def readint64(f: IO[bytes]) -> int:
    return int.from_bytes(f.read(8), 'little', signed=True)


def readshort(f: IO[bytes]) -> int:
    return int.from_bytes(f.read(2), 'little', signed=True)


def readsize_t(f: IO[bytes]) -> int:
    return int.from_bytes(f.read(8), 'little')


def readuint64(f: IO[bytes]) -> int:
    return int.from_bytes(f.read(8), 'little')


def readword(f: IO[bytes]) -> int:
    return int.from_bytes(f.read(2), 'little')


def readlen(f: IO[bytes]) -> int:
    le = 0
    b = f.read(1)
    while b[0] == 255:
        le += 1
        b = f.read(1)
    if le == 0:
        f.seek(-1, 1)
        return 0
    if le > 1:
        b += f.read(le - 1)
    return int.from_bytes(b, 'little')


def readwstr(f: IO[bytes]) -> str:
    f.read(2)
    si = readlen(f)
    if si == 0:
        return ''
    return f.read(si * 2).decode('UTF16')


def writebool(f: IO[bytes], i: bool) -> int:
    return writebyte(f, int(i))


def writebyte(f: IO[bytes], i: int) -> int:
    return f.write(i.to_bytes(1, 'little'))


def writeint(f: IO[bytes], i: int) -> int:
    return f.write(i.to_bytes(4, 'little', signed=True))


def writeint64(f: IO[bytes], i: int) -> int:
    return f.write(i.to_bytes(8, 'little', signed=True))


def writeshort(f: IO[bytes], i: int) -> int:
    return f.write(i.to_bytes(2, 'little', signed=True))


def writeuint64(f: IO[bytes], i: int) -> int:
    return f.write(i.to_bytes(8, 'little'))


def writeword(f: IO[bytes], i: int) -> int:
    return f.write(i.to_bytes(2, 'little'))


def callen(c: str) -> bytes:
    t = len(c)
    r = max(ceil(t.bit_length() / 8), 1)
    return b'\xff' * r + t.to_bytes(r, 'little')


def writewstr(f: IO[bytes], c: str) -> int:
    r = f.write(b'\xff\xfe')
    r += f.write(callen(c))
    r += f.write(c.encode('UTF16')[2:])
    return r

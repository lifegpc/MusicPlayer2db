from music_player2.carchive import (
    readbyte,
    readint,
    readwstr,
    writebool,
    writeint,
    writewstr,
)
from music_player2.exception import NoMorePathError
from music_player2.file_mode import FileMode
from music_player2.pathinfo import PathInfo, SortMode


class RecentPathFile:
    def __init__(self, fn: str, mode: FileMode = FileMode.READ) -> None:
        self._mode = mode
        self.__version = 2
        self.__si = 0
        self.__i = 0
        self.__hi: int = None
        if mode == FileMode.READ:
            self._f = open(fn, 'rb')
        else:
            self._f = open(fn, 'wb')
            self.__write_headers()
            self.__te = self._f.tell()

    def __enter__(self):
        return self

    def __exit__(self, typ, value, trace):
        if hasattr(self, '_f'):
            if self._f:
                self._f.close()

    def __iter__(self):
        if self._mode != FileMode.READ:
            raise ValueError('iter can only used when reading file.')
        if self.__hi is None:
            raise ValueError('parse() is needed calling before iter.')
        self._f.seek(self.__hi, 0)
        self.__i = 0
        return self

    def __next__(self):
        if self.__i >= self.__si:
            raise StopIteration
        return self.read()

    def __write_headers(self):
        self._f.seek(0, 0)
        writeint(self._f, self.__si)
        writeint(self._f, self.__version)

    def parse(self):
        if self._mode != FileMode.READ:
            raise ValueError('parse() can only used when reading file.')
        if not hasattr(self, '_f') or self._f is None:
            raise ValueError('File not opened.')
        self.__si = readint(self._f)
        b = self._f.read(2)
        self._f.seek(-2, 1)
        if b != b'\xff\xfe':
            self.__version = readint(self._f)
        self.__hi = self._f.tell()

    def read(self) -> PathInfo:
        if self._mode != FileMode.READ:
            raise ValueError('read() can only used when reading file.')
        if self.__i >= self.__si:
            raise NoMorePathError()
        pt = readwstr(self._f)
        p = PathInfo(pt)
        p.track = readint(self._f)
        p.position = readint(self._f)
        p.sort_mode = SortMode(readint(self._f))
        if self.version >= 2:
            p.descending = bool(readbyte(self._f))
        p.track_num = readint(self._f)
        p.total_time = readint(self._f)
        if self.version >= 1:
            p.contain_sub_folder = bool(readbyte(self._f))
        self.__i += 1
        return p

    def write(self, p: PathInfo):
        if self._mode != FileMode.WRITE:
            raise ValueError('write() can only used when writing file.')
        if not hasattr(self, '_f'):
            raise ValueError('File not opened.')
        self._f.seek(self.__te, 0)
        writewstr(self._f, p.path)
        writeint(self._f, p.track)
        writeint(self._f, p.position)
        writeint(self._f, p.sort_mode.value)
        writebool(self._f, p.descending)
        writeint(self._f, p.track_num)
        writeint(self._f, p.total_time)
        writebool(self._f, p.contain_sub_folder)
        self.__te = self._f.tell()
        self.__si += 1
        self.__write_headers()

    @property
    def version(self):
        return self.__version

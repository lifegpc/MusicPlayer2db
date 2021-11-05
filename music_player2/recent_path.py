from music_player2.carchive import readbyte, readint, readwstr
from music_player2.pathinfo import PathInfo, SortMode


class NoMorePathError(Exception):
    pass


class RecentPathFile:
    def __init__(self, fn: str) -> None:
        self._f = open(fn, 'rb')
        self.__version = 0
        self.__si = 0
        self.__i = 0

    def __enter__(self):
        return self

    def __exit__(self, typ, value, trace):
        if hasattr(self, '_f'):
            if self._f:
                self._f.close()

    def parse(self):
        if not hasattr(self, '_f') or self._f is None:
            raise ValueError('File not opened.')
        self.__si = readint(self._f)
        b = self._f.read(2)
        self._f.seek(-2, 1)
        if b != b'\xff\xfe':
            self.__version = readint(self._f)

    def read(self) -> PathInfo:
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

    @property
    def version(self):
        return self.__version

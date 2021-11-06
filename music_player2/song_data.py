from music_player2.carchive import (
    readbyte,
    readint,
    readint64,
    readshort,
    readsize_t,
    readuint64,
    readword,
    readwstr,
    writebool,
    writebyte,
    writeint,
    writeint64,
    writeshort,
    writeuint64,
    writeword,
    writewstr,
)
from music_player2.exception import NoMoreSongDataError
from music_player2.file_mode import FileMode
from music_player2.song_data_info import SongDataInfo


class SongDataFile:
    def __init__(self, fn: str, mode: FileMode = FileMode.READ) -> None:
        self._mode = mode
        if mode == FileMode.READ:
            self._f = open(fn, 'rb')
        else:
            self._f = open(fn, 'wb')
        self.__data_version = '2.730'
        self.__si = 0
        self.__i = 0
        self.__hi: int = None
        self.__te: int = 0
        if mode == FileMode.WRITE:
            self.__write_header()

    def __enter__(self):
        return self

    def __exit__(self, typ, value, trace):
        if hasattr(self, '_f'):
            if self._f:
                self._f.close()

    def __len__(self):
        return self.__si

    def __iter__(self):
        if self._mode != FileMode.READ:
            raise ValueError('iter can only used when reading file.')
        if self.__hi is None:
            raise ValueError('parse() is needed calling before iter.')
        self.__i = 0
        self._f.seek(self.__hi, 0)
        return self

    def __next__(self):
        if self.__i >= self.__si:
            raise StopIteration
        return self.read()

    def __write_header(self):
        if self.__hi is None:
            writewstr(self._f, self.__data_version)
            self.__hi = self._f.tell()
            self.__te = self.__hi + 4
        else:
            self._f.seek(self.__hi, 0)
        writeint(self._f, self.__si)

    @property
    def data_version(self) -> str:
        return self.__data_version

    def read(self) -> SongDataInfo:
        if self._mode != FileMode.READ:
            raise ValueError('read() can only used when reading file.')
        if self.__i >= self.__si:
            raise NoMoreSongDataError()
        fn = readwstr(self._f)
        t = readint(self._f)
        s = SongDataInfo(fn, t)
        if self.data_version >= '2.691':
            s.bitrate = readshort(self._f)
        else:
            s.bitrate = readint(self._f)
        s.title = readwstr(self._f)
        s.artist = readwstr(self._f)
        s.album = readwstr(self._f)
        s.year = readwstr(self._f)
        s.comment = readwstr(self._f)
        s.genre = readwstr(self._f)
        s.genre_idx = readbyte(self._f)
        if self.data_version >= '2.66':
            s.track = readint(self._f)
        else:
            s.track = readbyte(self._f)
        if self.data_version >= '2.691':
            s.tag_type = readbyte(self._f)
        else:
            s.tag_type = readint(self._f)
        s.song_id = readwstr(self._f)
        if self.data_version >= '2.64':
            s.listen_time = readint(self._f)
            s.info_acquired = readbyte(self._f)
        if self.data_version == '2.661':
            self._f.seek(1, 1)  # 1 bool
        if self.data_version >= '2.663' and self.data_version < '2.690':
            self._f.seek(2, 1)  # 2 bool
        if self.data_version >= '2.690':
            s.flags = readword(self._f)
        if self.data_version >= '2.680':
            s.last_played_time = readint64(self._f)
        if self.data_version >= '2.692':
            s.lyric_file = readwstr(self._f)
        if self.data_version >= '2.700':
            s.modified_time = readuint64(self._f)
        if self.data_version >= '2.720':
            s.rating = readbyte(self._f)
        if self.data_version >= '2.730':
            s.freq = readint(self._f)
            s.bits = readbyte(self._f)
            s.channels = readbyte(self._f)
        self.__i += 1
        return s

    def parse(self):
        if self._mode != FileMode.READ:
            raise ValueError('parse() can only used when reading file.')
        if not hasattr(self, '_f'):
            raise ValueError('File not opened.')
        self.__data_version = readwstr(self._f)
        if self.data_version >= '2.664':
            self.__si = readint(self._f)
        else:
            self.__si = readsize_t(self._f)
        self.__hi = self._f.tell()

    def write(self, s: SongDataInfo):
        if self._mode != FileMode.WRITE:
            raise ValueError('write() can only used when writing file.')
        if not hasattr(self, '_f'):
            raise ValueError('File not opened.')
        self._f.seek(self.__te, 0)
        writewstr(self._f, s.file_path)
        writeint(self._f, s.length)
        writeshort(self._f, s.bitrate)
        writewstr(self._f, s.title)
        writewstr(self._f, s.artist)
        writewstr(self._f, s.album)
        writewstr(self._f, s.year)
        writewstr(self._f, s.comment)
        writewstr(self._f, s.genre)
        writebyte(self._f, s.genre_idx)
        writeint(self._f, s.track)
        writebyte(self._f, s.tag_type)
        writewstr(self._f, s.song_id)
        writeint(self._f, s.listen_time)
        writebool(self._f, s.info_acquired)
        writeword(self._f, s.flags)
        writeint64(self._f, s.last_played_time)
        writewstr(self._f, s.lyric_file)
        writeuint64(self._f, s.modified_time)
        writebyte(self._f, s.rating)
        writeint(self._f, s.freq)
        writebyte(self._f, s.bits)
        writebyte(self._f, s.channels)
        self.__te = self._f.tell()
        self.__si += 1
        self.__write_header()

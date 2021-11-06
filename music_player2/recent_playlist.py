from music_player2.carchive import readint, readwstr
from music_player2.exception import NoMorePlayListError
from enum import Enum, unique


@unique
class PlaylistType(Enum):
    PT_USER = 0
    PT_DEFAULT = 1
    PT_FAVOURITE = 2
    PT_TEMP = 3

    def __str__(self):
        if self.value == self.PT_USER.value:
            return '用户'
        if self.value == self.PT_DEFAULT.value:
            return '默认'
        if self.value == self.PT_FAVOURITE.value:
            return '喜欢'
        if self.value == self.PT_TEMP.value:
            return '临时'


class PlaylistInfo:
    def __init__(self, track: int, position: int, track_num: int,
                 total_time: int, typ: PlaylistType, name: str = None) -> None:
        self.track = track
        self.position = position
        self.track_num = track_num
        self.total_time = total_time
        self.type = typ
        self.name = name

    def __str__(self):
        return f"""播放列表类型: {self.type}
名称：{self.name if self.name else self.type}
上次播放/总曲目: {self.track + 1}/{self.track_num}
上次播放位置/总时长: {self.position}/{self.total_time}"""


class RecentPlayListFile:
    def __init__(self, fn: str) -> None:
        self._f = open(fn, 'rb')
        self.__version: int = None
        self.__type: PlaylistType = None

    def __enter__(self):
        return self

    def __exit__(self, typ, value, trace):
        if hasattr(self, '_f'):
            if self._f:
                self._f.close()

    def parse(self):
        if not hasattr(self, '_f') or self._f is None:
            raise ValueError('File not opened.')
        self.__version = readint(self._f)
        self.__type = PlaylistType(readint(self._f))
        self.__i = 0
        self.__j = 0
        self.__si: int = None

    def read(self) -> PlaylistInfo:
        if self.__i == 0:
            track = readint(self._f)
            position = readint(self._f)
            track_num = readint(self._f)
            total_time = readint(self._f)
            p = PlaylistInfo(track, position, track_num, total_time,
                             PlaylistType.PT_DEFAULT)
            self.__i += 1
            return p
        if self.__i == 1 and self.version >= 2:
            track = readint(self._f)
            position = readint(self._f)
            track_num = readint(self._f)
            total_time = readint(self._f)
            p = PlaylistInfo(track, position, track_num, total_time,
                             PlaylistType.PT_FAVOURITE)
            self.__i += 1
            return p
        if self.__i == 2 and self.version >= 3:
            track = readint(self._f)
            position = readint(self._f)
            track_num = readint(self._f)
            total_time = readint(self._f)
            p = PlaylistInfo(track, position, track_num, total_time,
                             PlaylistType.PT_TEMP)
            self.__i += 1
            return p
        if self.__si is None:
            self.__si = readint(self._f)
        if self.__j >= self.__si:
            raise NoMorePlayListError()
        name = readwstr(self._f)
        track = readint(self._f)
        position = readint(self._f)
        track_num = readint(self._f)
        total_time = readint(self._f)
        p = PlaylistInfo(track, position, track_num, total_time, self.__type,
                         name)
        self.__j += 1
        return p

    @property
    def type(self):
        return self.__type

    @property
    def version(self):
        return self.__version

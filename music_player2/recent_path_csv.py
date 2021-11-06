from music_player2.csv import UTF8_BOM, readField, writeField
from music_player2.exception import NoMorePathError
from music_player2.file_mode import FileMode
from music_player2.pathinfo import PathInfo, SortMode
from music_player2.timestr import parsetimestr, totimestr


class RecentPathCSVFile:
    def __init__(self, fn: str, mode: FileMode = FileMode.WRITE) -> None:
        self._mode = mode
        if mode == FileMode.READ:
            self._f = open(fn, 'r', encoding='UTF8')
            if '\ufeff' != self._f.read(1):
                self._f.seek(0, 0)
            ll = readField(self._f)
            if len(ll) != 8:
                raise ValueError(f'8 columns is needed. Headers: {ll}')
            self.__hi = self._f.tell()
        else:
            self._f = open(fn, 'wb')
            self._f.write(UTF8_BOM)
            writeField(self._f, "位置", "上次播放的曲目", "上次播放的位置", "排序模式", "音频文件数量", "总时长", "包含子文件夹", "降序排列")  # noqa: E501

    def __enter__(self):
        return self

    def __exit__(self, typ, value, trace):
        if hasattr(self, '_f'):
            if self._f:
                self._f.close()

    def __iter__(self):
        if self._mode != FileMode.READ:
            raise ValueError('iter can only used when reading file.')
        self._f.seek(self.__hi, 0)
        return self

    def __next__(self):
        try:
            return self.read()
        except NoMorePathError:
            raise StopIteration

    def read(self) -> PathInfo:
        if self._mode != FileMode.READ:
            raise ValueError('read() can only used when reading file.')
        r = readField(self._f)
        if r is None:
            raise NoMorePathError()
        if len(r) != 8:
            raise ValueError(f'8 columns is needed. data: {r}')
        p = PathInfo(r[0])
        p.track = int(r[1])
        p.position = parsetimestr(r[2])
        p.sort_mode = SortMode(int(r[3]))
        p.track_num = int(r[4])
        p.total_time = parsetimestr(r[5])
        p.contain_sub_folder = bool(int(r[6]))
        p.descending = bool(int(r[7]))
        return p

    def write(self, p: PathInfo):
        if self._mode != FileMode.WRITE:
            raise ValueError('write() can only used when writing file.')
        if not hasattr(self, '_f'):
            raise ValueError('File not opened.')
        writeField(self._f, p.path, p.track, totimestr(p.position), p.sort_mode, p.track_num, totimestr(p.total_time), p.contain_sub_folder, p.descending)  # noqa: E501

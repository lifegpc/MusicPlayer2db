from typing import Optional


class SongDataInfo:
    def __init__(self, f: str, length: int) -> None:
        if not isinstance(f, str) or f == '':
            raise ValueError('File path is needed')
        self.__file_path = f
        self.__length = length
        self.__data = {}

    def __str__(self):
        return f'''文件路径： {self.__file_path}
时长： {self.__length}ms
{self.__data}'''

    @property
    def album(self) -> str:
        if 'album' in self.__data:
            return self.__data['album']
        else:
            return ''

    @album.setter
    def album(self, v: Optional[str]):
        if v is None:
            if 'album' in self.__data:
                del self.__data['album']
        elif isinstance(v, str):
            self.__data['album'] = v
        else:
            raise TypeError()

    @property
    def artist(self) -> str:
        if 'artist' in self.__data:
            return self.__data['artist']
        else:
            return ''

    @artist.setter
    def artist(self, v: Optional[str]):
        if v is None:
            if 'artist' in self.__data:
                del self.__data['artist']
        elif isinstance(v, str):
            self.__data['artist'] = v
        else:
            raise TypeError()

    @property
    def bitrate(self) -> int:
        if 'bitrate' in self.__data:
            return self.__data['bitrate']
        else:
            return 0

    @bitrate.setter
    def bitrate(self, v):
        if v is None:
            if 'bitrate' in self.__data:
                del self.__data['bitrate']
        elif isinstance(v, (int, float)):
            self.__data['bitrate'] = round(v)
        else:
            raise TypeError()

    @property
    def bits(self) -> int:
        if 'bits' in self.__data:
            return self.__data['bits']
        else:
            return 0

    @bits.setter
    def bits(self, v):
        if v is None:
            if 'bits' in self.__data:
                del self.__data['bits']
        elif isinstance(v, (int, float)):
            self.__data['bits'] = round(v)
        else:
            raise TypeError()

    @property
    def channels(self) -> int:
        if 'channels' in self.__data:
            return self.__data['channels']
        else:
            return 0

    @channels.setter
    def channels(self, v):
        if v is None:
            if 'channels' in self.__data:
                del self.__data['channels']
        elif isinstance(v, (int, float)):
            self.__data['channels'] = round(v)
        else:
            raise TypeError()

    @property
    def comment(self) -> str:
        if 'comment' in self.__data:
            return self.__data['comment']
        else:
            return ''

    @comment.setter
    def comment(self, v: Optional[str]):
        if v is None:
            if 'comment' in self.__data:
                del self.__data['comment']
        elif isinstance(v, str):
            self.__data['comment'] = v
        else:
            raise TypeError()

    @property
    def file_path(self) -> str:
        return self.__file_path

    @file_path.setter
    def file_path(self, v: str) -> str:
        if isinstance(v, str) and v != '':
            self.__file_path = v
        else:
            raise TypeError()

    @property
    def flags(self) -> int:
        if 'flags' in self.__data:
            return self.__data['flags']
        else:
            return 0

    @flags.setter
    def flags(self, v):
        if v is None:
            if 'flags' in self.__data:
                del self.__data['flags']
        elif isinstance(v, (int, float)):
            self.__data['flags'] = round(v)
        else:
            raise TypeError()

    @property
    def freq(self) -> int:
        if 'freq' in self.__data:
            return self.__data['freq']
        else:
            return 0

    @freq.setter
    def freq(self, v):
        if v is None:
            if 'freq' in self.__data:
                del self.__data['freq']
        elif isinstance(v, (int, float)):
            self.__data['freq'] = round(v)
        else:
            raise TypeError()

    @property
    def genre(self) -> str:
        if 'genre' in self.__data:
            return self.__data['genre']
        else:
            return ''

    @genre.setter
    def genre(self, v: Optional[str]):
        if v is None:
            if 'genre' in self.__data:
                del self.__data['genre']
        elif isinstance(v, str):
            self.__data['genre'] = v
        else:
            raise TypeError()

    @property
    def genre_idx(self) -> int:
        if 'genre_idx' in self.__data:
            return self.__data['genre_idx']
        else:
            return 255

    @genre_idx.setter
    def genre_idx(self, v):
        if v is None:
            if 'genre_idx' in self.__data:
                del self.__data['genre_idx']
        elif isinstance(v, (int, float)):
            self.__data['genre_idx'] = round(v)
        else:
            raise TypeError()

    @property
    def info_acquired(self) -> bool:
        if 'info_acquired' in self.__data:
            return self.__data['info_acquired']
        else:
            return False

    @info_acquired.setter
    def info_acquired(self, v):
        if v is None:
            self.__data['info_acquired'] = False
        else:
            self.__data['info_acquired'] = bool(v)

    @property
    def last_played_time(self) -> int:
        if 'last_played_time' in self.__data:
            return self.__data['last_played_time']
        else:
            return 0

    @last_played_time.setter
    def last_played_time(self, v):
        if v is None:
            if 'last_played_time' in self.__data:
                del self.__data['last_played_time']
        elif isinstance(v, (int, float)):
            self.__data['last_played_time'] = round(v)
        else:
            raise TypeError()

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, v):
        if isinstance(v, int):
            self.__length = v
        elif isinstance(v, float):
            self.__length = round(v)
        else:
            raise TypeError()

    @property
    def listen_time(self) -> int:
        if 'listen_time' in self.__data:
            return self.__data['listen_time']
        else:
            return 0

    @listen_time.setter
    def listen_time(self, v):
        if v is None:
            if 'listen_time' in self.__data:
                del self.__data['listen_time']
        elif isinstance(v, (int, float)):
            self.__data['listen_time'] = round(v)
        else:
            raise TypeError()

    @property
    def lyric_file(self) -> str:
        if 'lyric_file' in self.__data:
            return self.__data['lyric_file']
        else:
            return ''

    @lyric_file.setter
    def lyric_file(self, v: Optional[str]):
        if v is None:
            if 'lyric_file' in self.__data:
                del self.__data['lyric_file']
        elif isinstance(v, str):
            self.__data['lyric_file'] = v
        else:
            raise TypeError()

    @property
    def modified_time(self) -> int:
        if 'modified_time' in self.__data:
            return self.__data['modified_time']
        else:
            return 0

    @modified_time.setter
    def modified_time(self, v):
        if v is None:
            if 'modified_time' in self.__data:
                del self.__data['modified_time']
        elif isinstance(v, (int, float)):
            self.__data['modified_time'] = round(v)
        else:
            raise TypeError()

    @property
    def rating(self) -> int:
        if 'rating' in self.__data:
            return self.__data['rating']
        else:
            return 255

    @rating.setter
    def rating(self, v):
        if v is None:
            if 'rating' in self.__data:
                del self.__data['rating']
        elif isinstance(v, (int, float)):
            self.__data['rating'] = round(v)
        else:
            raise TypeError()

    @property
    def song_id(self) -> str:
        if 'song_id' in self.__data:
            return self.__data['song_id']
        else:
            return ''

    @song_id.setter
    def song_id(self, v: Optional[str]):
        if v is None:
            if 'song_id' in self.__data:
                del self.__data['song_id']
        elif isinstance(v, str):
            self.__data['song_id'] = v
        else:
            raise TypeError()

    @property
    def tag_type(self) -> int:
        if 'tag_type' in self.__data:
            return self.__data['tag_type']
        else:
            return 0

    @tag_type.setter
    def tag_type(self, v):
        if v is None:
            if 'tag_type' in self.__data:
                del self.__data['tag_type']
        elif isinstance(v, (int, float)):
            self.__data['tag_type'] = round(v)
        else:
            raise TypeError()

    @property
    def title(self) -> str:
        if 'title' in self.__data:
            return self.__data['title']
        else:
            return ''

    @title.setter
    def title(self, v: Optional[str]):
        if v is None:
            if 'title' in self.__data:
                del self.__data['title']
        elif isinstance(v, str):
            self.__data['title'] = v
        else:
            raise TypeError()

    @property
    def track(self) -> int:
        if 'track' in self.__data:
            return self.__data['track']
        else:
            return 0

    @track.setter
    def track(self, v):
        if v is None:
            if 'track' in self.__data:
                del self.__data['track']
        elif isinstance(v, (int, float)):
            self.__data['track'] = round(v)
        else:
            raise TypeError()

    @property
    def year(self) -> str:
        if 'year' in self.__data:
            return self.__data['year']
        else:
            return ''

    @year.setter
    def year(self, v: Optional[str]):
        if v is None:
            if 'year' in self.__data:
                del self.__data['year']
        elif isinstance(v, str):
            self.__data['year'] = v
        else:
            raise TypeError()

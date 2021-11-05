from enum import Enum, unique


@unique
class SortMode(Enum):
    SM_FILE = 0
    SM_PATH = 1
    SM_TITLE = 2
    SM_ARTIST = 3
    SM_ALBUM = 4
    SM_TRACK = 5
    SM_TIME = 6


class PathInfo:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.track = 0
        self.position = 0
        self.sort_mode = SortMode(0)
        self.track_num = 0
        self.total_time = 0
        self.contain_sub_folder = False
        self.descending = False

    def __str__(self) -> str:
        return f'''位置：{self.path}
上次播放的曲目：{self.track}
上次播放的位置：{self.position}
排序模式：{self.sort_mode}
音频文件数量：{self.track_num}
音频文件总时长：{self.total_time}
包含子文件夹：{self.contain_sub_folder}
降序排序：{self.descending}'''

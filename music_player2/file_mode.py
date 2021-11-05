from enum import Enum, unique


@unique
class FileMode(Enum):
    READ = 0
    WRITE = 1

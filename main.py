from pathlib import Path
import time
from decouple import config

HOME_FOLDER = config('HOME_FOLDER')

HOME_PATH = Path(HOME_FOLDER)


def list_generator(pattern='*'):
    name_max_len = len((max(HOME_PATH.iterdir(), key=lambda x: len(x.name))).name)
    size_max_len = len(str((max(HOME_PATH.iterdir(), key=lambda x: x.stat().st_size)).stat().st_size))
    for item in HOME_PATH.glob(pattern):
        name = item.name.ljust(name_max_len, ' ')
        size = str(item.stat().st_size).ljust(size_max_len, ' ')
        created_at = time.ctime(item.stat().st_ctime)
        modified_at = time.ctime(item.stat().st_mtime)
        result = f'{name} | {size} bytes | Created at {created_at} | Modified at {modified_at}'
        yield result


def list_items(pattern='*'):
    for item in list_generator(pattern):
        print(item)


def remove(file):
    file_path = HOME_PATH.joinpath(file)
    if file_path.exists():
        file_path.unlink()
        print(f'{file} deleted')
    else:
        print(f'{file} file was not found')


list_items('*.py')
remove('test.txt')
list_items()

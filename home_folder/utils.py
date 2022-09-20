import time
from pathlib import Path
from decouple import config


HOME_FOLDER = config('HOME_FOLDER')
HOME_PATH = Path(HOME_FOLDER)


def check_file(path):
    result = ''
    file = Path(path)
    home_file = HOME_PATH.joinpath(file.name)
    if not file.exists():
        result = f'File {file.name} does not exists'
        return False, file, result
    if home_file.exists():
        result = f'File {home_file.name} already exists'
        return False, file, result
    return True, file, result


def list_generator(pattern):
    if '*' not in pattern:
        pattern = f'*{pattern}*'
    name_max_len = len((max(HOME_PATH.iterdir(), key=lambda x: len(x.name))).name)
    size_max_len = len(str((max(HOME_PATH.iterdir(), key=lambda x: x.stat().st_size)).stat().st_size))
    files = list(HOME_PATH.glob(pattern))
    if files:
        for file in files:
            name = file.name.ljust(name_max_len, ' ')
            size = str(file.stat().st_size).ljust(size_max_len, ' ')
            created_at = time.ctime(file.stat().st_ctime)
            modified_at = time.ctime(file.stat().st_mtime)
            yield f'{name} | {size} bytes | Created at {created_at} | Modified at {modified_at}'
    else:
        yield f'files with pattern "{pattern}" was not found'


def man():
    com = '''
    >add: add file to filesys.
    Syntax: add <file_path/file_name>,
    >remove: remove file from filesys,
    Syntax: remove <file_name>,
    >list: list of files or pattern match files,
    Syntax: list "optional"<pattern>,
    >exit: to exit program,
    Systax: exit
    >help: for manual
    Syntax: help
    '''
    return com




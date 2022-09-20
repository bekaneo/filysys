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
    files = list(HOME_PATH.glob(pattern))
    if files:
        for file in files:
            yield file.name
    else:
        yield f'files with pattern "{pattern}" was not found'


def man():
    manual = '''
    >add: add file to filesys.
    Syntax: add <file_path/file_name>,
    >remove: remove file from filesys,
    Syntax: remove <file_name>,
    >list: list of files or pattern match files,
    Syntax: list "optional"<'pattern'>,
    >exit: to exit program,
    Systax: exit
    >help: for manual
    Syntax: help
    '''
    return manual




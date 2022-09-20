from pathlib import Path

from decouple import config

HOME_FOLDER = config('HOME_FOLDER')
HOME_PATH = Path(HOME_FOLDER)


def list_generator(pattern):
    if '*' not in pattern:
        pattern = f'*{pattern}*'
    files = list(HOME_PATH.glob(pattern))
    if files:
        for file in files:
            yield file.name
    else:
        yield f'file not found'


def man(args):
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
    print(manual)

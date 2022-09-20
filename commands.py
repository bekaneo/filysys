import shutil
from pathlib import Path

from utils import list_generator, HOME_PATH


def add_item(path):
    file = Path(path)
    home_file = HOME_PATH.joinpath(file.name)
    if not file.exists():
        exit(f'File {file} was not found')
    if home_file.exists():
        exit(f'File {file} already exists')
    shutil.copy2(file, HOME_PATH)
    print(f'{file.name} added to folder')


def list_items(pattern='*'):
    for item in list_generator(pattern):
        print(item)


def remove_item(file):
    file_path = HOME_PATH.joinpath(file)
    if file_path.exists():
        file_path.unlink()
        print(f'{file} deleted')
    else:
        print(f'{file} file was not found')



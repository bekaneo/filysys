import shutil

from utils import list_generator, check_file, HOME_PATH


def add_item(path):
    exists, file, text = check_file(path)
    if not exists:
        return text

    shutil.copy2(file, HOME_PATH)
    return f'{file.name} added to folder'


def list_items(pattern='*'):
    for item in list_generator(pattern):
        print(item)


def remove_item(file):
    file_path = HOME_PATH.joinpath(file)
    if file_path.exists():
        file_path.unlink()
        return f'{file} deleted'

    return f'{file} file was not found'

import sys

from commands import add_item, remove_item, list_items, HOME_PATH
from utils import man

if not HOME_PATH.exists():
    exit(f'Folder {HOME_PATH} does not exists')

commands = {
    'add': add_item,
    'remove': remove_item,
    'list': list_items,
    'help': man
}

if __name__ == '__main__':
    _, command, *args = sys.argv
    if command not in commands:
        exit(f'command {command} was not found')
    if len(args) > 1:
        exit(f'command {" ".join(sys.argv[1:])} was not found')
    commands[command](*args)





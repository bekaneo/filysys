from main import add_item, remove_item, list_items
from utils import HOME_PATH, man

commands = {
    'add': add_item,
    'remove': remove_item,
    'list': list_items,
    'exit': exit,
    'help': man
}

if __name__ == '__main__':
    while True:
        command = input(f'{HOME_PATH}>: ').split()
        try:
            if command[0] == 'exit':
                commands[command[0]]()
            if command[0] == 'help':
                commands[command[0]]()
            if command[0] == 'add':
                print(commands[command[0]](command[1]))
            if command[0] == 'remove':
                print(commands[command[0]](command[1]))
            if command[0] == 'list':
                try:
                    commands[command[0]](command[1])

                except IndexError:
                    commands[command[0]]()

        except (KeyError, IndexError):
            print(f'Command {command} does not exists. help - for manual')
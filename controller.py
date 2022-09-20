from commands import add_item, remove_item, list_items
from utils import man

commands = {
    'add': add_item,
    'remove': remove_item,
    'list': list_items,
    'exit': exit,
    'help': man
}


def controller(args):
    if args[1] == 'exit':
        commands[args[1]]()
    elif args[1] == 'help':
        print(commands[args[1]]())
    elif args[1] == 'add':
        print(commands[args[1]](args[2]))
    elif args[1] == 'remove':
        print(commands[args[1]](args[2]))
    elif args[1] == 'list':
        try:
            commands[args[1]](args[2])

        except IndexError:
            commands[args[1]]()
    else:
        print(f'Command <{" ".join(args[1:])}> was not found. help - for manual')

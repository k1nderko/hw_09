EXIT = ['exit', 'goodbye', 'close']
run = True
lst_input = []
contacts = {}

def command_error(func):
    def inner(input_com):
        if func(input_com) == None:
            return 'Unknown command. Enter help for to see all commands'
        return func(input_com)
    return inner  

def args_error(func):
    def inner():
        try:
            return func()
        except IndexError:
            return 'No name or phone, try again or enter help'
    return inner

def hello() -> str:
    return 'How can I help you?'

def help() -> str:
    return '''
    hello -- just hello
    add name phone -- add new contact
    change name phone -- change contact phone
    phone name -- print contact phone
    show all -- print all contacts
    exit, goodbye, close -- exit program'''
    pass

@args_error
def add() -> str:
    phone = lst_input[1]
    name = lst_input[0]
    contacts[name] = phone
    return f'Contact {name} added successfully.'

@args_error
def change() -> str:
    phone = lst_input[1]
    name = lst_input[0]
    contacts[name] = phone
    return f'Contact {name} modified successfully.'

@args_error
def phone() -> str:
    name = lst_input[0]
    return contacts.get(name)

def show_all() ->str:
    for_print = ''
    for k, v in contacts.items():
        for_print += k + ' ' + v + '\n'
    return for_print.strip()

COMMANDS = {hello: 'hello', help: 'help', add: 'add', change: 'change', phone: 'phone', show_all: 'show all'}

@command_error
def command_handler(input_com: str):
    if input_com.lower() in EXIT:
            global run
            run = False
            return 'Good bye'

    for func, val in COMMANDS.items():
        if input_com.lower().startswith(val):
            global lst_input
            lst_input = input_com.replace(val, '').strip().split(' ')
            return func()

def main():
    while run:
        command = input('>>>')
        print(command_handler(command))
        lst_input.clear()
        

if __name__ == '__main__':
    main()
import re

# Here we have the first command prompt, where the player will give their initial input
def prompt_inicial():
    print('*********************************')
    print('*** Welcome to Project Tabula ***')
    print('*********************************')
    while True:
        round_counter = 0
        if not round_counter:
            print('What time is it? (HH:MM)')
            user_input = input('>')
            time_valid = time_ok(user_input)
            if time_valid:
                input_split = user_input.split(':')
                print(f'{input_split[0]}:{input_split[1]}')
            else:
                raise ValueError('Hour not valid!')
        while True:
            print('What is your wish?')
            user_input = input('>').lower()
            input_split = user_input.split(' ')
            (load, save, check, add, heal, atrib,
             skip, round_pass, exitgame, help_c) = command_bool(input_split)
            if load:
                print('1')
            elif save:
                print('2')
            elif check:
                print('3')
            elif add:
                print('4')
            elif heal:
                print('5')
            elif atrib:
                print('6')
            elif skip:
                print('7')
            elif round_pass:
                print('8')
                break
            elif exitgame:
                print('Goodbye')
                exit()
            elif help_c:
                print('Commands:')
                print('load: load especified gamestate. -- save: save gamestate. -- check: check specified character.')
                print('add: add specified character to the stage. -- heal: heal character an specified amount.')
                print('atrib: do an atribute check on a character. -- skip: skip an amount of time (rounds).')
                print('exit: exit game. save gamestate before, please. -- help: acquire command explanation.')
        round_counter =+ 1

def time_ok(user_input):
    time_pattern = re.compile('[0-9][0-9]:[0-9][0-9]')
    time_true = time_pattern.match(user_input)
    input_split = user_input.split(':')
    hour_ok = 0 <= int(input_split[0]) <= 24
    minute_ok = 0 <= int(input_split[1]) <= 60
    time_ok = time_true and hour_ok and minute_ok
    return time_ok

def command_bool(input_split):
    load = input_split[0] == 'load'
    save = input_split[0] == 'save'
    check = input_split[0] == 'check'
    add = input_split[0] == 'add'
    heal = input_split[0] == 'heal'
    atrib = input_split[0] == 'atrib'
    skip = input_split[0] == 'skip'
    round_pass = input_split[0] == ''
    exitgame = input_split[0] == 'exit'
    help_c = input_split[0] == 'help'
    return load, save, check, add, heal, atrib, skip, round_pass, exitgame, help_c

prompt_inicial()

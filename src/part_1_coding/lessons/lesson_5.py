"""
If statement, loop control with for and while
"""

tutorial = input('Chose your sector: (1 / 2 / 3): ')

if tutorial == 1:
    x = int(input('Enter a number: '))
    email_list = ['gmail.com', 'yahoo.com', 'hotmail.com', 'anaf.com']

    if x == 10:
        print('X este egal cu 10')
        if input('Introduceti email: ') == 'popescu@gmail.com':
            print('Adresa email este corecta')
        elif input('Introduceti email: ').split('@')[1] in ['gmail.com', 'yahoo.com', 'hotmail.com', 'anaf.com']:
            # elif '@gmail.com' in input('Introduceti email: '):
            # elif input('Introduceti email: ') in '@gmail.com':
            print('Email format ok, but wrong user')
        else:
            print('No condition found')
    elif x == 20:
        print('X este egal cu 20')
    elif x == 30:
        print('X este egal cu 30')
    else:
        print(f'X != {x}')


elif tutorial == 2:
    a, y = True, False

    if not y:
        print('Welcome!')


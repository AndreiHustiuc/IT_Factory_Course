m_rabbit = int(input('Number of male rabbits: '))
f_rabbit = int(input('Number of female rabbits: '))

if m_rabbit > 0 and f_rabbit > 0:
    x = input('Do you want to breed (Yes/No): ').lower()
    if x == 'no':
        print('Keep male and female rabbit apart!')



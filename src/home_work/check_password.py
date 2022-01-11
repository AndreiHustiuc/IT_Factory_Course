from src.part_1_coding.lessons.generate_pwd import generate_pwd


def check_password(strg):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '1234567890'
    special = '!@#$%^&*()_'

    lower_check = False
    upper_check = False
    number_check = False
    special_check = False

    for i in lower:
        for j in strg:
            if i == j:
                lower_check = True

    for i in upper:
        for j in strg:
            if i == j:
                upper_check = True

    for i in number:
        for j in strg:
            if i == j:
                number_check = True

    for i in special:
        for j in strg:
            if i == j:
                special_check = True

    if lower_check and upper_check and number_check and special_check:
        return "Password is strong"
    elif lower_check and upper_check or lower_check and number_check or lower_check and special_check:
        return "Password is medium"
    elif lower_check or number_check or upper_check or special_check:
        return 'Password is weak'


sample = generate_pwd(20, numbers=True, lower_case=True)

print(check_password(sample))

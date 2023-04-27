import requests, termcolor, sys, colorama, hashlib, string


def password_analyser(userinput):
    symbol_characters = tuple(string.punctuation)
    colorama.init()
    common_passwords = requests.get(
        "https://raw.githubusercontent.com/ThirumalR-78/CommonPasswordsList/main/commonPasswordsList.txt"
    )

    if (common_passwords.status_code == 200):
        termcolor.cprint('Succesfully Imported Common Password List!', 'green')
    else:
        termcolor.cprint(
            f'Error Requesting Common Password List! Code: {common_passwords.status_code}',
            'red')
        sys.exit()

    hash_value = hashlib.sha1(userinput.encode())
    sha_1 = hash_value.hexdigest()
    haveibeenpwnedapi = requests.get(
        f"https://api.pwnedpasswords.com/range/{sha_1[:5]}")

    if (haveibeenpwnedapi.status_code == 200):
        termcolor.cprint('Succesfully Contacted HaveIBeenPwned API!', 'green')
    else:
        termcolor.cprint(
            f'Error Contacting HaveIBeenPwned API! Code: {haveibeenpwnedapi.status_code}',
            'red')
        sys.exit()

    for line in haveibeenpwnedapi.text.splitlines():
        colonsplit = line.split(':')
        if (colonsplit[0].lower() == sha_1[5:]):
            pwned = True
            break
    else:
        pwned = False

    for line in common_passwords.text.splitlines():
        if (line == userinput):
            is_a_common_password = True
            break
    else:
        is_a_common_password = False

    if (len(userinput) >= 8): over_eight_characters = True
    else: over_eight_characters = False

    for letter in userinput:
        if (letter.isupper()):
            contains_upper_case = True
            break
    else:
        contains_upper_case = False

    for letter in userinput:
        if (letter in symbol_characters):
            symbol_used = True
            break
    else:
        symbol_used = False


    print("---------------------------------------")
    returnValue = []
    if (is_a_common_password): 
        termcolor.cprint('Is a common password!', 'red')
        returnValue.append('Is a common password!\n')
    else: termcolor.cprint('Is not a common password!', 'green')
    if (over_eight_characters):
        termcolor.cprint('Contains eight or more characters!', 'green')
        returnValue.append('Contains eight or more characters!\n')
    else:
        termcolor.cprint('Below eight characters!', 'red')
        returnValue.append('Below eight characters!\n')
    if (contains_upper_case):
        termcolor.cprint('Contains atleast one uppercase character!', 'green')
        returnValue.append('Contains atleast one uppercase character!\n')
    else:
        termcolor.cprint('Does not contain at least one uppercase character!',
                         'red')
        returnValue.append('Does not contain at least one uppercase character!\n')
    if (symbol_used):
        termcolor.cprint('Contains a symbol!', 'green')
        returnValue.append('Contains a symbol!\n')
    else: 
        termcolor.cprint('Does not contain a symbol!', 'red')
        returnValue.append('Does not contain a symbol!\n')
    if (pwned): 
        termcolor.cprint(f'Password Pwned {colonsplit[1]} times! ', 'red')
        returnValue.append(f'Password Pwned {colonsplit[1]} times!\n')
    else: 
        termcolor.cprint("Password not Pwned!", 'green')
        returnValue.append('Password not Pwned!')
    print("---------------------------------------")
    result = " ".join(returnValue)
    # with open('data.txt', 'w') as f:
    # f.write('hello world')
    return result

def Function1(input_text):
    res = password_analyser(input_text)
    # result = " ".join(returnValue)
    # with open('data.txt', 'r') as f:
    # data = f.read()

    # print(data)
    return res

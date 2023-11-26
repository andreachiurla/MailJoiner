# COLORS
green = '\u001b[92m'
red = '\u001b[31m'
underline = '\u001b[4m'
yellow = "\033[93m"
reset = "\033[0m"


def ask_present(f):
    presents = []
    y = 1
    while 1:
        user = input(f"Presente {y}: ")
        if user == '0':
            break
        if user != '':
            if search_in_file(f, user):
                presents.append(int(user))
                print(presents)
                y += 1
            else:
                print(red, "Identificatore non trovato", reset)

    return presents


def to_string(f, presents):
    concat_strings = ""
    separator = ""
    f.seek(0)
    while 1:
        line = f.readline()
        if line == "":
            return concat_strings
        for present in presents:
            if int(line[0]) == int(present):
                line = line.replace("\n", "")
                line = line[2:]
                concat_strings += separator + line
                separator = ", "
                break


def add_mail(f):
    address_list = []

    while 1:
        mail_to_add = input(yellow + "Inserisci un indirizzo mail: " + reset)
        if mail_to_add == "":
            break
        while 1:
            n_address = input(yellow + "Inserisci il numero identificativo: " + reset)
            if not search_in_file(f, n_address):    # if the number hasn't been used yet
                address_list.append(n_address + " " + mail_to_add + "\n")
                break
            else:
                print(red, "Numero già utilizzato", reset)

    f.writelines(address_list)


# Searches int in a file
# If 'to_search' is in the first position of the line returns True, otherwise False
def search_in_file(f, to_search):
    f.seek(0)
    while 1:
        line = f.readline()
        if line == "":
            return False
        if line[0] == to_search:
            return True

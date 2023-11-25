# COLORS
green = '\u001b[92m'
red = '\u001b[31m'
underline = '\u001b[4m'
yellow = "\033[93m"
reset = "\033[0m"

def ask_present():
    presents = []
    y = 1
    while 1:
        user = int(input(f"Presente {y}: "))
        if user == 0:
            break
        if user != '':
            presents.append(int(user))
            print(presents)
        y += 1

    return presents


def to_string(f, presents):
    concat_strings = ""
    separator = ""

    while 1:
        line = f.readline()

        if line == "":
            return concat_strings

        line = search_in_file(f, line[0])
        for present in presents:
            if int(line[0]) == present:
                line = line.replace("\n", "")
                line = line[2:]
                concat_strings += separator + line
                separator = ", "
                break


def add_mail(f):
    address_list = []
    str = ""

    while 1:
        mail_to_add = input(yellow + "Inserisci un indirizzo mail: " + reset)
        if mail_to_add == "":
            break
        n_address = input(yellow + "Inserisci il numero identificativo: " + reset)
        if is_free(f, n_address):
            address_list.append("\n" + mail_to_add)
            print(address_list)
        else:
            print(red, "Numero già utilizzato", reset)


    f.writelines(address_list)


def search_in_file(f, to_search):
    return "linea file"
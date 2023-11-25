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
        mail_to_add = input("Inserisci un indirizzo mail: ")
        if mail_to_add == "":
            break
        address_list.append("\n" + mail_to_add)
        print(address_list)

    f.writelines(address_list)

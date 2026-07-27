while True:
    name = input('Insert you name: ')
    list_names = ['Isaque', 'Sthefani', "Yago"]

    if name in list_names:
        print(f'O nome "{name}" está na lista')
    else:
        print(f'O nome "{name}" não está na lista')
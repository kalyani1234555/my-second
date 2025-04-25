from metal_data import medals_table


options = {
    'C': ('country', lambda d: d['country'], False),
    'G': ('gold medals', lambda d: d['gold'], True),
    'S': ('silver medals', lambda d: d['silver'], True),
    'B': ('bronze medals', lambda d: d['bronze'], True),
    'R': ('rank', lambda d: d['rank'], False),
}

  while True:
    for option, (description, *_) in options.items():
        print(f'{option}: Sort by {description}')
    print('Invalid choices will exit.')

    choice = input('Please select an option: ').upper()

    # if choice == 'C':
    #     medals_table.sort(key=lambda d: d['country'])
    # elif choice == 'G':
    #     medals_table.sort(key=lambda d: d['gold'], reverse=True)
    # elif choice == 'S':
    #     medals_table.sort(key=lambda d: d['silver'], reverse=True)
    # elif choice == 'B':
    #     medals_table.sort(key=lambda d: d['bronze'], reverse=True)
    # elif choice == 'R':
    #     medals_table.sort(key=lambda d: d['rank'])

    description, function, reverse = options.get(choice, (None, None, None))
    if description:
        medals_table.sort(key=function, reverse=reverse)

    else:
        break

    # print(f'Sorted by {options[choice][0]}')
    print(f'Sorted by {description}')
    for row in range(10):
        print(medals_table[row])

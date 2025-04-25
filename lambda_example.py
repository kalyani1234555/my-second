from metal_data import medals_table


def sort_key(d : dict) -> str:
    return d['country']


medals_table.sort(key=sort_key)
print(medals_table)


# lambda:

medals_table.sort(key=lambda d: d['country'])
print(medals_table)

# for row in range(10):
#     print(medals_table[row])

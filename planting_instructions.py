from data import plants_list


def sort_perennials(item) -> str:
    # print(item)
    if item.lifecycle.casefold() == 'perennial':
        # print(item.name)
        return '1' + item.name
    else:
        return '0' + item.name


# plants_list.sort(key=sort_perennials)
# plants_list.sort(key=lambda item: '1' + item.name if item.lifecycle.casefold() == 'perennial' else '0' + item.name)
plants_list.sort(key=lambda item: '1' + item.name if item.lifecycle == 'Perennial' else '0' + item.name)

with open('planting_instructions.txt', 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        # where_to_plant = 'window box' if plant.lifecycle == 'perennial' else 'garden'
        where_to_plant, who = ('window box', 'me') if plant.lifecycle == 'Perennial' else ('garden', 'gardener')
        print(f"{plant.name}:{where_to_plant}: {who}", file=output_file)


# where_to_plant = 'window box'
# for plant in plants_list:
#     if plant.lifecycle == 'perennial':
#         where_to_plant = 'window box'
#     else:
#         where_to_plant = 'garden'
#   print(f"{plant.name}:{where_to_plant}", file=output_file)

# with open('planting_instructions.txt', 'w', encoding='utf-8') as output_file:
#     for plant in plants_list:
#         # where_to_plant = 'window box' if plant.lifecycle == 'perennial' else 'garden'
#         if plant.lifecycle == 'perennial':
#             where_to_plant = 'window box'
#             who = 'me'
#         else:
#             where_to_plant = 'garden'
#             who = 'garderner'
#         print(f"{plant.name}: {where_to_plant}: {who}", file=output_file)

from data import basic_plants_list, plants_list
from collections import namedtuple

print(plants_list[0])
# print(basic_plants_list[0])
# for plant in basic_plants_list:
#     print(plant[0])

for plant in plants_list:
    print(plant.name, plant[1])

print()

# example = plants_list[0]
# print(example)
# example = example._replace(lifecycle='Annual')
# print(example)

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')
print(example)

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)

p2 = p1._replace(x=3, y=5)
print(p2)

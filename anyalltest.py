plants_list = ["Tree", "Grass", "Flower"]
found_grass = False
for plant in plants_list:
    if plant == "Grass":
        found_grass = True
        break
print(any(found_grass))

all_plants = ["Tree", "Grass", "Flower"]
all_are_plants = True
for plant in all_plants:
    if not isinstance(plant, str):
        all_are_plants = False
        break
print(all(all_are_plants))

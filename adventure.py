available_exists = ["north", "south", "east", "west"]

chosen_exist = ""

while chosen_exist not in available_exists:
    chosen_exist = input("please choose a direction: ")
    if chosen_exist.casefold() == "quit":
        print("game over")
        break


# print("aren't you glad you got out of there")
else:
    print("aren't you glad you got out of there")

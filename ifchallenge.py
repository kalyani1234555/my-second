name = input("Enter your name: ")
age = int(input("How old are you? "))

if 18 <= age <= 30:
    print("welcome to club 18-30 holidays, {}".format(name))
else:
    print("I'm sorry, our holidays are only for cool people")

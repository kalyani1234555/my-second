name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("you are old enough to vote")
else:
    print("please come back in {0} years".format(18 - age))

message = "you are old enough to vote" if age >= 18 else "please come back in {0} years".format(18 - age)
print(message)

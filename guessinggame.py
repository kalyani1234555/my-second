import random


def get_integer(prompt):
    """
    Get an integer from standard Input (stdin).

    The function will continue the looping, and prompting
    the user, until a valid 'int' is entered.

    :param prompt:The String that the user will see, when
        they're prompted to enter the value
    :return: The integer that the user enters.
    """
    while True:  # if we get correct value it will terminate
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

help(get_integer)
highest = 1000
answer = random.randint(1, highest)
print(answer)  # ToDo: Remove after testing
# answer = 5
guess = 0

print("please guess number between 1 and {}: ".format(highest))
while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        print("well done, you guessed correct")
        break
    else:
        if guess < answer:
            print("please guess the higher")
        else:  # guess must be greater than the answer
            print("please guess the lower")

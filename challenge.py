import sys


def getint(prompt):
    while True:
        try:
            # number = int(input("Please enter a number "))
            number = int(input(prompt))
            return number
        except EOFError:
            sys.exit(1)
        # except Exception:
        except: # should really be except ValueError
            print("Invalid number entered, please try again")
        # except ValueError:
        #     print("Invalid number entered, please try again")
        # except EOFError:
        #     sys.exit(1)
        finally:
            print("The finally clause always execute")


first_number = getint("Please enter first number")
second_number = getint("Please enter second number")

# print(getint())

# x = int(input("Enter a number "))

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("you can't divide by zero")
    sys.exit(2)

else:
    print("Division performed successfully")
# finally:
#     print("Division performed successfully")

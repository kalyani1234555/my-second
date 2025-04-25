print("please choose your option from the list below:")
print("1.\t Learn python")
print("2.\t Learn Java")
print("3.\t Go swimming")
print("4.\t Have dinner")
print("5.\t Go to bed")
print("0.\t exit")
choice = "-"

# while True:
#     choice = input()
#
#     if choice == "0":
#       pass
#
#     elif choice in "12345":
#         print("you got {} value".format(choice))
#     else:
#         print("please choose your option from the list below:")
#         print("1.\t Learn python")
#         print("2.\t Learn Java")
#         print("3.\t Go swimming")
#         print("4.\t Have dinner")
#         print("5.\t Go to bed")
#         print("0.\t exit")


while choice != 0:
    if choice in "12345":
        print("you got {} value".format(choice))
        break
    else:
        print("please choose your option from the list below:")
        print("1.\t Learn python")
        print("2.\t Learn Java")
        print("3.\t Go swimming")
        print("4.\t Have dinner")
        print("5.\t Go to bed")
        print("0.\t exit")
    choice = input()


#

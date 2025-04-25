low = 1
high = 1000

print("please think of a number between {} and {}".format(low, high))
input("press Enter to start")

guesses = 1
# while True:
while low != high:
    # print("\t guessing in the range of {} to {}".format(low, high))
    guess = low + (high-low) // 2
    high_low = input("my guess is {}. should i guess higher or lower? enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    if high_low == "h":
        # guess higher.the low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # guess lower. the high end of the range becomes less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("i got it {} guesses!". format(guesses))
        break
    else:
        print("please enter h, l, or c")
    # guesses = guesses + 1
    guesses += 1
else:
    print("you thought the number {}".format(high))
    print("i got it {} guesses!". format(guesses))

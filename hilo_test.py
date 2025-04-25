LOW = 1
HIGH = 10

# print("please think of a number between {} and {}".format(low, high))
# input("press Enter to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\t guessing in the range of {} to {}".format(low, high))
        guess = low + (high-low) // 2
        # high_low = input("my guess is {}. should i guess higher or lower? enter h or l, or c if my guess was correct"
    #                  .format(guess)).casefold()
        # if high_low == "h":
        if guess < answer:

            # guess higher.the low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:

            # guess lower. the high end of the range becomes less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("i got it {} guesses!". format(guesses))
            # break
            return guesses
        # else:
        #   print("please enter h, l, or c")
        # guesses = guesses + 1
        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses,  1
    elif number_of_guesses == max_guesses:
        correct_count += 1
print("I guessed without being told {} times. Max {} guesses."
      .format(correct_count, max_guesses))

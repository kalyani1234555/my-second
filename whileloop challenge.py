import random
highest = 10
answer =random.randint(1,highest)
print(answer)
guess = 0
print("please guess number between 1 and {}: ".format(highest))


while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess == answer:
        print("well done, you guessed correct")
        break

    else:
        if guess < answer:
            print("please guess the higher")
        else:  # guess must be greater than the answer
            print("please guess the lower")

import random
highest = 10
answer = random.randint(1,highest)
print(answer)
guess=0

while guess != answer:
    guess = int(input())
    if guess == 0:
        print("quit the game")
        break

    if guess == answer:
        print("guess is correct")
        break

    else:
        if guess < answer:
            print("guess the higher value")
        else:
            print("guess the lower value")

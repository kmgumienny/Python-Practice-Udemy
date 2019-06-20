# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 1000
answer = random.randint(1, highest)

# print("Please guess a number between 1 and {}: ".format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:  # guess must be greater than number
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    else:  # guess must be greater than number
        print("Please guess lower")
    guess = int(input("Guess another number between 0 and {}. ".format(highest)))
    continue
print("Congratulations, you won!")
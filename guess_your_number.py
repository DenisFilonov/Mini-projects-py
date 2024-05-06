import random as r
import time as t

try:
    digit = int(input("Enter a number: "))
    if digit <= 0 or digit > 100:
        print("Please, input a number between 1 and 100 including both end points, and try again")
        quit()

    i = int(input("Enter attempt count: "))
    if i <= 0:
        print("Please, input correctly attempts count, and try again")
        quit()
except ValueError:
    print("Error: Please, input an integer number and/or attempt count value")
    quit()

no_cheat = 2
guess = 0
j = i

# This while needs to let the user have a conversation with program
while i > 0:
    print(f"\nAttempt #{i}:")
    guess = r.randint(1, 100)
    print(f"Is your number is: {guess}? ")

    check = input("Input plus or minus: ")
    if check == '+' or check == '-':
        if digit == guess and check == '+':
            print(f"There are {j - i} tries I used to guess your number. Thanks for playing!")
            # One of the possible end of this program
            break

        elif digit == guess and check == '-':
            # If user lied
            print("\nBut, that's not true. I guessed the number right.")
            quit()
        else:
            if digit != guess and check == '-':
                print("\nFine! Let's continue guessing the number")
                i -= 1
            else:
                # When user trying to motivate you, but didn't say you truth...
                print("\nBut, that's not true...")
                quit()

    # If check's equals something else than + or -
    else:
        '''
        Once or twice you can input something wrong, until program will show you guessed number.
        So this case starts to be a bug, because the amount of tries is not decrease in this situation.
        The point of this else block is:
            * to avoid cheating and prevent the program guess the number without count of attempts
        '''

        if no_cheat != 0:
            print("\nI will not count this attempt, but you should input + or - ")
            no_cheat -= 1
        else:
            print("\nStop kidding me :)")
            break

# Second of the possible end of this program
print("\n\nOkay then, let me guess your number by myself")
count = 0
t.sleep(3)
while True:
    guess = r.randint(1, 100)
    count += 1
    if guess == digit:
        print("Found!")
        break
t.sleep(2)
print(f"There are {count} tries I used to guess your number. Thanks for playing!")

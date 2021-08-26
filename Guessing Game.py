import random

name = input('Hello. What is your name?\n')

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNum = random.randint(1,20)

for i in range(1, 7):
    guess = int(input('Take a guess:\n'))

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break #this condition is correct guess.

if guess == secretNum:
    print('Good job, ' + name + '! You guessed my number in ' + str(i) + ' guesses!')
else:
    print('Sorry, ' + name +', but the number I was thinking of was: ' + str(secretNum))


    

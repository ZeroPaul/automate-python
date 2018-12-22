import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

for guessesTaken in range (1, 7):
    guess = int(input('Take a guess: '))
    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job! You guessed my number in %s guesses!' % (guessesTaken))
else:
    print('Nope. The number I was thinking of was %s' % (secretNumber))

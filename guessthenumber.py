""" Guess the number program """

# 1.Set Up
import random
secretNumber = random.randint(1, 30)
print('I am thinking of a number between 1 and 30.')

# 2. Imput
'''ask the player to guess six possible numbers'''
for guessesTaken in range(1, 7):
    print('Guess which one but you only have six trys ~')
    guess = int(input())

    if guess == 314:
        print('You gonna get me pie or are you just flirting. ;)')
    if guess < secretNumber:
        print('Hehe..Too low like your IQ.')
    elif guess > secretNumber:
        print('Too high try again next time.')

    else:
        break
    ''' The brake only works if the answer is right'''


# 4. Output
if guess == secretNumber:
    print('Boo! You guessed it in ' + str(guessesTaken) + ' guesses! No fair :(')
else:
    print('Not even close! Try harder. The number I was thinking of was ' + str(secretNumber))

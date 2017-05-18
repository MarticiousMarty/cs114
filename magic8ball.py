print("What yould you like to know?")
input()

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Not with that hair cut'
    elif answerNumber == 2:
         return 'It might it might not.'
    elif answerNumber == 3:
           return 'Yes'
    elif answerNumber == 4:
           return 'To tipst to be misty'
    elif answerNumber == 5:
           return 'Ask your mom'
    elif answerNumber == 6:
            return 'Maybe try it with a smile next time huh'
    elif answerNumber == 7:
           return 'Heck no!'
    elif answerNumber == 8:
           return 'Go get a puppy insted'
    elif answerNumber == 9:
           return 'Grab a beer on me...or you, I dont have hands..or money.'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

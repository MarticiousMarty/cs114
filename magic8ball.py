print("Ask a question, any question??")
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
         return 'Go ask your mom'
    elif answerNumber == 6:
         return 'Maybe try it with a smile next time huh'
    elif answerNumber == 7:
         return 'Heck no!'
    elif answerNumber == 8:
         return 'Go get a puppy insted'
    elif answerNumber == 9:
         return 'Grab a beer on me...or you, I dont have hands..or money.'
    elif answerNumber == 10:
         return 'Sure why not'
    elif answerNumber == 11:
         return 'Shia labeouf that thing man'

random_int= random.randint(1, 11)
fortune = getAnswer(random_int)
print(fortune)

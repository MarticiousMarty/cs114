# Dracula exercise from text book

print('Are you a Vampier? yes or no (use lower case)')
is_vampire = input()

# you wann start with no as its easy
# make it an if statmnet
if is_vampire == 'no':
    print("Oh...Sorry but your to fleshy to hang out with.")
    exit()
# else is the next transition
else:
    print("How old are you?")
    age = int(input())

if age > 100:
    print("I hope you don't get a sun burn, that would be a pain in the neck...")

if age < 100:
    print("Wow! You barly have your traning fangs...")

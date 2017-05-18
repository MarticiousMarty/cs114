"""Convert a miles per gallons to kilomiters"""

# 1. set up
miles_per_kilometer = 1.609344
kilometers_per_miles = 0.621371

# 2. Input
print('How many miles?')
miles = float(input())

# 3. Transform
# sn: killometers goes first not miles
kilometers = miles * miles_per_kilometer
# 4. output
print(str(miles) + ' miles is ' + str(kilometers) + ' kilometers.')

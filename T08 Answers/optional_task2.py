'''asks user questions about weather to help them decide what to wear'''

print("Please answer the following questions with either y or n for inputs")

#get user input and sets variable to a boolean based on users answer
temp_over_20 = input('Is the temperature over 20 degrees? (y/n)').lower()
temp_over_20 = True if temp_over_20 == 'y' else False

weekend = input('Is today a weekend day? (y/n)').lower()
weekend = True if weekend == 'y' else False

sunny = input('Is today a sunny day? (y/n)').lower()
sunny = True if sunny == 'y' else False

#creates outfit based on user answers
shirt = "short-sleeved shirt" if temp_over_20 else "long-sleeved shirt"
pants = "shorts" if weekend else "jeans"
coat_or_hat = "cap" if sunny else "raincoat"

#outputs answer to user
print("Based on your answers, you should wear a {0}, {1} and a {2}, have a nice day!".format(shirt, pants, coat_or_hat))
"""This program takes a string input from the user, and outputs a count
of the letters"""

#get user input
word = input("Please input a word:\n")
#set up result dict
result = {}

#loop through input
for letter in word:
    #if letter already in result then just increment value by 1
    if letter in result:
        result[letter] += 1
    #if letter not already in result then add as a key with a value of 1
    else:
        result.update({letter: 1})

#output result to user
print(result)

'''This program takes a string input from user and outputs
whether or not the input is a palindrome'''

#get user input
word = input("Please enter a word\n")

#compare string with its reversed version using string slicing, if they match then word is a palindrome
if word == word[::-1]:
    print("your word is a palindrome!")

else:
    print("your word is not a palindrome!")
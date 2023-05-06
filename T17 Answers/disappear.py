'''asks user for a string and set of characters they want removed
then prints input string without these characters'''

#get sentence from user
sentence = input("Please enter a sentence\n")

#get chars to remove
chars_to_remove = input("Please enter what characters you want removed from your sentence\n")

#get individual chars as a list
chars_list = [char for char in chars_to_remove]


#remove chars from sentence
for char in chars_list:
    sentence = sentence.replace(char, '')


#output final result
print(sentence)



'''This program reads in a string and makes each alternate
character uppercase and the other characters lowercase, then prints.
It also prints the same sentence with every other word capitalized'''

#get input
sentence = input("Please enter a sentence to convert\n")

#initialize list to store changed sentence
new_sentence = []

#loop through string
for i in range(0, len(sentence)):
    if i % 2 == 0:
        #if i is even, capitalize and append the letter in sentence[i] to the new sentence
        new_sentence.append(sentence[i].upper())
    else:
        #if i is not even, append the lowercase letter to new_sentence
        new_sentence.append(sentence[i].lower())

#join letters into single string and output
print("".join(new_sentence))

#takes same sentence, and convert every other word to uppercase, while rest are lowercase

#split sentence into individual words
word_list = sentence.split(' ')

#initialize list to hold changed words
changed_word_list = []

#loop through word_list
for i in range(0, len(word_list)):
    #if i is odd, change word at position i in word list to uppercase, and append to output list
    if i % 2 == 1:
        changed_word_list.append(word_list[i].upper())

    # if i is even, change word at position i in word list to lowercase, and append to output list
    else:
        changed_word_list.append(word_list[i].lower())

#join list into single string 
print(" ".join(changed_word_list))
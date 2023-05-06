'''this program takes a sentence as input from the user, then outputs
each word on a seperate line'''

#get input
sentence = input("Please enter a sentence")

#split sentence into a list
word_list = sentence.split(' ')


#loop through list and output each word on a new line
for word in word_list:
    print(word)
#get user input
str_manip = input('Please enter a sentence\n')

#prints length
print(len(str_manip))

#replace last letter and any occurences of this letter with @

last_letter = str_manip[-1]
print(str_manip.replace(last_letter, '@'))

#print last 3 letters backwards

print(str_manip[:-4: -1])

#create word from first 3 chars and last 2 chars of str_manip
beg = str_manip[0:3]
end = str_manip[-2:]
new_word = beg + end
print(new_word)
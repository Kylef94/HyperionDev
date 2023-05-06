def daysofweek():
    '''prints days of the week'''
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        print(day)

def replace():
    '''replaces every second word with hello'''
    sentence = input("Please enter a sentence")
    output = []
    for i, word in enumerate(sentence.split(' ')):
        if i % 2 == 1:
            word = "Hello"

        output.append(word)

    print(' '.join(output))

daysofweek()
replace()
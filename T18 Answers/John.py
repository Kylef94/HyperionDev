#initialize list to store names
names = []

#initialize boolean for while loop
john = False

#keep asking for names until user enters "John"

while not john:
    # take user input as string
    user_input = input("Please enter a name: ")

    #when input is john, end loop
    if user_input.lower() == 'john':
        john = True
    else:
        #if output isnt john, add to names list
        names.append(user_input)

#output to user
print(f"Incorrect names: {names}")
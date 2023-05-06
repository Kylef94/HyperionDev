# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.
 
name = "Tim"
surname = " Jones"
age = 21

#string was not fomatted correct(is was not in "") (Syntax error)
#previous declaration didnt use f-string which made output badly formatted, changed to f-string for better formatting (logical error)
fullMessage = f"{name}{surname} is {age} years old"

#print statement was missing brackets (Syntax error)
print(fullMessage)

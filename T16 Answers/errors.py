# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#fixed missing brackets (syntax error)
print("Welcome to the error program")

#fixed indentation issue, lines were indented incorrectly which prevented run (syntax error)
print("\n")

#assignment was done using equality operator, corrected to assignment operator (syntax error)
#cast to int failed as ageStr contains letters, removed "years old" from ageStr to allow casting in age variable (syntax error)
ageStr = "24" #I'm 24 years old.
age = int(ageStr)

#print used age var however ints cannot be concatenated to string, so changed to ageStr (syntax error)
#also added spaces as below print displayed as "I'm24yearsold", add spaces before and after concatenation (logical error)
print("I'm " + ageStr + " years old.")

three = "3"

#statement added an int (age) and string (three) variable, so cast three to int (syntax error)

answerYears = age + int(three)

# answerYears was contained in "" which would simply print string "answerYears" instead of var value, changed to f-string (syntax error)
print(f"The total number of years: {answerYears}")

#var answer was not defined, should be answerYears (syntax error)
#answer months only includes the 3 years added to answerYears, but output states 3 years and 6 months, so adding 6 here to ensure correct months calculated (logical error)
answerMonths = answerYears * 12 + 6

#answerMonths wasnt cast to string for concatenation (syntax error)
print("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old")

#HINT, 330 months is the correct answer


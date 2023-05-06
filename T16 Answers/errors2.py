# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#animal var was string initialised without "", added these. (Syntax error)
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#string was just normal string, changed to f-string so var values are added to output (Syntax error)
#also vars number_of_teeth and animal_type were in each other's positions in string, switched them so output makes sense (logical error)
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

#print statement was missing brackets (Syntax error)
print(full_spec)


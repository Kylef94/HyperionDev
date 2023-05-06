'''this program demonstrates two compilation errors,
a runtime error and a logical error'''

#compilation error 1

name == kyle #uses equal instead of assignment operator, and doesn't enclose string in ""

return = input("input your return address") #uses a reserved word as a variable name which throws a compilation error

#compilation error 2

list = ['apple', 'orange', 'pear']

list.remove('blueberry') #trying to remove an element which isn't in a list will compile but throws a value error on runtime

#logical error
i = 1
while i < 10:
    print(i)
#without incrementing i on each loop, i will remain 1 and so this will form an infinite loop


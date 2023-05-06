
#uses while loop to count down from 20 to 0

#initialize var for while loop with starting val 20
num = 20

#loops through and prints each number, then decrements num on each loop
while num >= 0:
    print(num)
    num -= 1

#prints all even numbers between 1 and 20

for i in range(1,20):
    if i % 2 == 0:
        print(i)


#prints a small pyramid of *'s
#e.g.
#*
#**
#***
#****
#*****

for i in range(1,6):
    print('*' * i)

#finds gcd of two numbers

x = 60
y = 25

#GCD cannot be larger than the smaller number of the pair, so we will loop up to this number
if x > y:
    smaller_num = y
else:
    smaller_num = x

#loops through range, set end to +1 to ensure end number is included
for i in range(1, smaller_num + 1):
    #uses modulo to check divisibility
    if (x % i == 0) and (y % i == 0):
        gcd = i

#returns output to user
print(f"The GCD of {x} and {y} is {gcd}")

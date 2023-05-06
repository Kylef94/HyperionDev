#get user inputs

fav_rest = input('Please enter your favourite restaurant\n')
int_fav = int(input('Please enter your favourite number\n'))

print(fav_rest)
print(int_fav)

# try casting fav_rest to int
# this line will not work as python only allows strings to be cast to int if the characters in the string are numeric
#eg if string was '10' then would work fine

print(int(fav_rest))



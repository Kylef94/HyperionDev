#initialize lists to hold names and birth dates
names = []
birth_dates = []

#read file
with open('DOB.txt', 'r') as f:

    #split file into seperate words then join names and DOBs into their respective lists
    for line in f:
        line = line.split()
        names.append(' '.join(line[0:2]))
        birth_dates.append(' '.join(line[2:5]))

#print lists
print("Name")
for name in names:
    print(name)

print()
print("Birthdate")
for date in birth_dates:
    print(date)

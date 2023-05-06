
def amazon(operation, nums):
    '''helper function to do the operation on the num lists and to encapsulate the switch logic'''
    match operation:
        case 'min':
            return f"the min of {nums} is {min(nums)}"
        case 'max':
            return f"the max of {nums} is {max(nums)}"
        case 'avg':
            return f"the avg of {nums} is {sum(nums) / len(nums)}"

#set list var for output
output = []

#read in data
with open("input.txt", 'r') as file:
    data = file.readlines()
    for line in data:
        #clean data and split
        line = line.split(":")
        line = [i.strip("ï»¿").strip("\n") for i in line]
        #convert nums into ints and split into a list
        nums = [int(i) for i in line[1].split(',')]

        #run the amazon helper function on the nums list, and append the result for output
        output.append(amazon(line[0], nums))

#append outputs to the output file
with open("output.txt", "w") as file:
    for line in output:
        file.write(line)
        file.write('\n')





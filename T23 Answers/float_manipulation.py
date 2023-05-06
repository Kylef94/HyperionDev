import statistics


#list to store user inputs
nums = []

#ask for numbers until 10 entered
while len(nums) <= 10:
    num = float(input("Please enter a number: "))
    nums.append(num)

#output sum, index of max, index of min, average and median
print(f"sum: {sum(nums)}")
print(f"index of max num: {nums.index(max(nums))}")
print(f"index of min num: {nums.index(min(nums))}")
print("average: {:.2f}".format(sum(nums) / len(nums)))
print(statistics.median(nums))
#to generate ints for lists
import random

#set up lists of integers using random

nums1 = [random.randint(1, 1000) for i in range(10)]
nums2 = [random.randint(1, 1000) for i in range(10)]

#set up nums3 list to store all numbers from nums1 and nums2
nums3 = nums1 + nums2

#sort each list
nums1.sort()
nums2.sort()
nums3.sort()

#convert each list to strings using list comprehension and write to file
with open("numbers1.txt", 'w') as file:
    to_write = [str(i) + '\n' for i in nums1]
    file.writelines(to_write)

with open("numbers2.txt", 'w') as file:
    to_write = [str(i) + '\n' for i in nums2]
    file.writelines(to_write)


#write nums3 to all_numbers.txt
with open("all_numbers.txt", 'w') as file:
    to_write = [str(i) + '\n' for i in nums3]
    file.writelines(to_write)


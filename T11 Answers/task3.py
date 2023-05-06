'''determines what award a triathlon participant should receive
based on time taken to complete
'''

#set const for qualifying time in minutes
QUAL_TIME = 100

#get times for each event and sum

swimming = float(input("Please input your time in the swimming event in minutes\n"))
cycling = float(input("Please input your time in the cycling event in minutes\n"))
running = float(input("Please input your time in the running event in minutes\n"))

total_time = swimming + cycling + running
print(f"Your total time for the triathlon was {total_time}")

#determine if award achieved
if total_time <= QUAL_TIME:
    print("Congratulations! You have been awarded the Provincial Colours")

elif total_time < (QUAL_TIME + 5):
    print("Congratulations! You have been awarded the Provincial Half Colours")

elif total_time < (QUAL_TIME + 10):
    print("Congratulations! You have been awarded the Provincial Scroll")

else:
    print("You did not achieve an award this time")


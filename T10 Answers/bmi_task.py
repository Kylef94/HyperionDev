'''this person takes users weight in kg and height in m and
calculates their BMI, its then tells user their BMI category(obese, overweight,normal or underweight)'''

weight = float(input("Please enter your weight in Kg\n"))
height = float(input("Please enter your height in M\n"))

#calculate BMI

bmi = weight / (height ** 2)

#check BMI category
if bmi >= 30:
    category = 'obese'

elif 30 > bmi >= 25:
    category = 'overweight'

elif 25 > bmi >= 18.5:
    category = 'normal weight'

else:
    category = 'underweight'

print(f"Thank you! your BMI is {bmi:.2f} and this indicates that you are {category}")
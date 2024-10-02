#Give weight and height in kilogram and meter
weight = float(input("Enter Weight in kilogram: "))
height = float(input("Enter Height in meter: "))

#Calculate BMI
bmi = round(weight / (height**2),1)

#Conditions
if bmi<18.5:
    result = "Under Weight"
elif bmi>=18.5 and bmi<=24.9:
    result = "Normal Weight"
elif bmi >=25 and bmi<=29.9:
    result = "Over weight"
elif bmi>=30 and bmi<=34.9:
    result = "Obesity"
elif bmi>=35 and bmi<=39.9:
    result = "Extreme Obesity"

print(result)
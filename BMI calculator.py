height = float(input("Enter your height in Meters: "))
weight = float(input("Enter your weight in Kilogram: "))

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print("Your BMI is Underweight")
elif bmi < 25:
    print("Your BMI is Normal or Healthy")
elif bmi < 30:
    print("Your BMI is Overweight")
elif bmi >= 30:
    print("You are Obese, HIT THE GYM!")

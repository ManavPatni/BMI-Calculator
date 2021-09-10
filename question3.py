# Created by Manav Patni
# Program to calculate BMI

height = float(input("Enter your height in m here:- "))
weight = float(input("Enter your weight in kg here:- "))

bmi = weight/height**2

if bmi <= 20:
    print("Your BMI is ", bmi, "\n", "You are under weight.",
          "\n", "Eat more and healthy food :( ")
elif bmi >= 21 and bmi <= 24:
    print("Your BMI is ", bmi, "\n", "You are doing well keep it up :)")
elif bmi >= 25 and bmi <= 27:
    print("Your BMI is ", bmi, "\n", "You are overweight.",
          "\n", "Do daily workout :( ")
elif bmi > 27:
    print("Your BMI is ", bmi, "\n", "Your in criticle condition.",
          "\n", "Take a medical consent as soon as possible :( ")
else:
    print("Something went wrong!!")

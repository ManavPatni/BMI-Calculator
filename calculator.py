# Created by Manav Patni
# Program to calculate BMI

height = float(input("Enter your height in cm here:- "))
weight = float(input("Enter your weight in kg here:- "))

bmi = weight / (height/100)**2

if bmi <= 18.4:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are over weight.")
elif bmi <= 34.9:
    print("You are severely over weight.")
elif bmi <= 39.9:
    print("You are obese.")
elif:
    print("You are severely obese.")
else:
    print("Something went wrong!!")

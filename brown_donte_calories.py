# Donte' Brown
# September 8th 2026
# This program is designed to estimate the average calories burned for a person when exercising.

# Inputs
age = int(input("Please enter your age: "))
weight = float(input("Please enter your weight in pounds: "))
heart_rate = int(input("Please enter your heart rate in beats per minute: "))
exercise_time = int(input("Please enter the length of your workout in minutes: "))

# Calories burned calculation
calories_burned = ((age*0.2757+weight*0.03295+heart_rate*1.0781-75.4991)*exercise_time)/8.368

# Output
print(f"Calories burned: {calories_burned:.2f} calories")
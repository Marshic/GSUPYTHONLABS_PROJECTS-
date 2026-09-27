# Donte' Brown
# September 8th 2026
# This program is designed to calculate the volume of a Sphere and the factorial of a randomly generated number between 1 and 10.


from math import pi, factorial
from random import randint
# Inputs
radius = float(input("Please enter the radius of the sphere: "))


# Calculate
volume = (4/3) * pi * (radius ** 3)
factorial_number = randint(1, 10)

# Output
print(f"The volume of a sphere with radius {radius} is: {volume:.2f}")
print(f"The factorial of {factorial_number} is {factorial(factorial_number)}")
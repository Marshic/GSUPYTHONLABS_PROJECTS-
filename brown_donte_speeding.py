# Donte' Brown   
# September 22nd 2026
# This program takes a speed limit and driving speed in miles per hour and outputs the traffic ticket amount

# Prompt the user
speed_limit = int(input("Please enter the speed limit for the road: "))
driving_speed = int(input("Please enter the vehicle's recorded speed: "))

# Calculations
difference = driving_speed - speed_limit

# Conditions
if driving_speed <= speed_limit - 10:
    ticket = 50
elif difference >= 6 and difference<= 20:
    ticket = 75
elif difference >=21 and difference<= 40:
    ticket = 150
elif difference > 40:
    ticket = 300
else:
    ticket = 0
print(f"The speeding fine is ${ticket}")
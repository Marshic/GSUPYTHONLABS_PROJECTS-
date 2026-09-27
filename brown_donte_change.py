# Donte' Brown
# September 8th 2026
# This program is designed to convert a user-entered number of cents into the fewest number of US coins of that amount.

# Floor for the outcome of whatever divided by 25
# Take the remainder of the last as the new cents and floor it by 10


# Calculations
cents = int(input("Please enter the number of cents: "))
quarters = cents // 25 
dimes = (cents % 25) // 10 
nickels = (cents % 25 % 10) // 5
pennies = (cents % 25 % 10 % 5) // 1

# Output
print(f"Coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")
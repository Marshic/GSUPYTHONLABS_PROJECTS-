# Donte' Brown  
# September 15th 2026
# This program formats a given phone number as input.

# Prompt user
phone_num = int(input("Please enter your phone number (10 digits): "))

# Calcualtions?
area_code = phone_num // 10000000

remainder = phone_num // 10000
prefix = remainder % 1000

line_number = phone_num % 10000
print(f"Phone Number: ({area_code}) {prefix}-{line_number}")
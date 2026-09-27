# Donte' Brown   
# September 22nd 2026
# This program will detect a Given a highway number, indicate whether it is a primary, auxiliary highway, or an invalid highway number

# Get inputs
highway = int(input("Please enter an inerstate number: "))


# Conditions
if highway >=1 and highway<=99:
    print("I-"+str(highway) + " is a primary highway")
    # Even primary highway
    if highway % 2 == 0:
        print("It runs east/west")
    # Odd primary highway
    else:
        print("It runs north/south")
#Aux Highway
elif highway >= 100 and highway<=999:
    # Get the last digit to determine which primary highway it serves
    primary = highway % 100
    if primary == 0:
        print(f"{highway} is not a valid highway number.")
    else:
        print(f"I-{highway} is auxiliary")
        if primary % 2 == 0:
            print(f"I-{primary} runs east/west.")
        else:
            print(f"I-{primary} runs north/south.")
else:
    print("Invalid highway number.")
""" Program: Introduction 
Donte Brown
This program is a simple calculator for a pizza party. """

# User prompts
num_ppl = int(input("Please enter the number of people attending the party: "))
num_pizza = int(input("Please enter the number of pizzas purchased for the party: "))
diameter = int(input("Please enter the diameter of the pizzas: "))
num_slices = int(input("Please enter the number of slices per pizza: "))
print()
print()
# Calculations
radius = diameter/2
total_area = 3.14 * radius * radius
per_person_area = total_area/num_ppl
total_slices = num_pizza * num_slices
slice_per = total_slices//num_ppl


# Display 
print (f"Total pizza area: {total_area:.2f} square inches")
print (f"Pizza area per person: {per_person_area:.2f} square inches")
print (f"Total number of slices: {total_slices}")
print (f"Slices per person: {slice_per}")
print()
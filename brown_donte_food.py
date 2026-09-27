# Donte' Brown  
# September 15th 2026
# This program simulates a point-of-sale device for a restaurant.

# Menu Dictionary
menu = {"Hot Dog":1.50,
              "Slice of Pizza":1.99,
              "Whole Pizza":9.95,
              "Soft Drink":0.59}

# Prompt the user
hot_dogs = (int(input("Please enter number of Hot Dogs: ")))
pizza_slices = (int(input("Please enter number of Pizza Slices: ")))
whole_pizzas = int(input("Please enter number of Whole Pizzas: "))
soft_drinks = int(input("Please enter number of Soft Drinks: "))

# Calculate
hot_dog_total = hot_dogs * menu["Hot Dog"]
pizza_slices_total = pizza_slices * menu["Slice of Pizza"]
whole_pizzas_total = whole_pizzas * menu["Whole Pizza"]
soft_drinks_total = soft_drinks * menu["Soft Drink"]

total_order = hot_dog_total + pizza_slices_total + whole_pizzas_total + soft_drinks_total


# Display to user
print()
print(f"The total cost of the order is ${total_order:.2f}")
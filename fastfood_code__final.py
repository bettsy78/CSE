Sandwich = ["chicken", "beef", "tofu"]
Sandwich_price = [5.25, 6.25, 5.75]
Beverage_list = ["no", "small", "medium", "large"]
Beverage_price = [0.00, 1.00, 1.75, 2.25]
Fries_list = ["no", "small", "medium", "large"]
Fries_price = [0.00, 1.00, 1.50, 2.00]
Ketchup_price = 0.25
total_price = 0.00
print("Welcome to the fast food order program!")
print("Please enter your order below.")

# Sandwich order
sandwich = input("\nWould you like a chicken, beef, or tofu sandwich? ")
selected_a_sandwich = False
sandwich_price = 0
if sandwich in Sandwich:
    selected_a_sandwich = True
    sandwich_price = Sandwich_price[Sandwich.index(sandwich)]

if selected_a_sandwich:
    print("You ordered a", sandwich, "sandwich")
else:
    print("Invalid sandwich choice!")

# Fries order
selected_fries = False
fries_price = 0
while not selected_fries:
    fries = input("\nWould you like fries with that? (no, small, medium, or large) ")
    if fries in Fries_list:
        selected_fries = True
        fries_price = Fries_price[Fries_list.index(fries)]
        print("You ordered", fries, "fries")
    else:
        print("Invalid fries choice! Please select again.")

# Drinks order
selected_drink = False
drink_price = 0
while not selected_drink:
    drink = input("\nWould you like a beverage? (no, small, medium, or large) ")
    if drink in Beverage_list:
        selected_drink = True
        drink_price = Beverage_price[Beverage_list.index(drink)]
        print("You ordered a", drink, "beverage")
    else:
        print("Invalid beverage choice! Please select again.")

# Calculate total price
total_price = sandwich_price + fries_price + drink_price

# Repeat final order to the customer
print("\nYour final order:")
print("\tSandwich:", sandwich)
print("\tFries:", fries)
print("\tDrink:", drink)
print("\tTotal price: $", total_price)

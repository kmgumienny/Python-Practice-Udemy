burgers = ["beef", "chicken", "spicy beans"]
toppings = ["cheege", "egg", "beans", "spam"]

for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)

print()

for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
    print(nested_meals)

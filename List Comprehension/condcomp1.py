menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["egg", "spam", "bacon"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# print(meals)
#
# x = 12
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

for meal in menu:
    print(meal, "contains sausage" if "sausage" in meal else "contains bacon" if "bacon" in meal else "contains egg")


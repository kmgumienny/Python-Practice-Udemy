menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["egg", "spam", "bacon"])
menu.append(["spam", "egg", "sausage", "spam"])
menu.append(["chicken", "chips"])


meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)

# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

def unit_check(question):
    valid_unit_list = [
        [""],
        ["g", "grams", "gram"],
        ["mg", "milligrams", "milligram"],
        ["kg", "kilograms", "kilogram"],
        ["mL", "millilitres", "ml", "mls", "millilitre"],
        ["L", "litres", "l", "litre"],
        ["quart", "quarts", "fl qt", "qt", "q"],
        ["pint", "pints", "fl pt", "pt", "p"],
        ["cup", "cups", "c"],
        ["tbsp", "tablespoons", "tablespoon", "tbs"],
        ["tsp", "teaspoons", "teaspoon"],
        ["lb", "pounds", "lbs", "pound"],
        ["stick", "sticks"],
        ["oz", "ounces", "ounce", "fl oz", "fluid ounces", "fluid ounce"]
    ]

    valid = False

    while not valid:
        response = input(question).lower()

        for var_list in valid_unit_list:
            if response in var_list:
                response = var_list[0]

                return response

        else:
            print("Error: Please enter a valid unit")


def int_check(question):
    valid = False

    while not valid:
        response = input(question)

        try:
            if float(response) <= 0:
                print("Error: Number must be more than 0")

            else:
                return response

        except ValueError:
            print("Error: Please enter a number")


valid_units_list = [
        [""],
        ["g", "grams", "gram"],
        ["mg", "milligrams", "milligram"],
        ["kg", "kilograms", "kilogram"],
        ["mL", "millilitres", "ml", "mls", "millilitre"],
        ["L", "litres", "l", "litre"],
        ["quart", "quarts", "fl qt", "qt", "q"],
        ["pint", "pints", "fl pt", "pt", "p"],
        ["cup", "cups", "c"],
        ["tbsp", "tablespoons", "tablespoon", "tbs"],
        ["tsp", "teaspoons", "teaspoon"],
        ["lb", "pounds", "lbs", "pound"],
        ["stick", "sticks"],
        ["oz", "ounces", "ounce", "fl oz", "fluid ounces", "fluid ounce"]
    ]
ingredients_list = ["flour", "milk", "eggs"]
units_list = []
amount_list = []
plural_units = []

for item in units_list:
    for x in valid_units_list:
        for y in x:
            plural = valid_units_list.index(item)
            plural_units.append(valid_units_list[plural][1])

print(plural_units)

for item in ingredients_list:
    for obj in plural_units:
        amount = int_check("How many " + obj + " of" + item + "? ")
        amount_list.append(float(amount))

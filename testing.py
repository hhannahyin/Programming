import csv

''' ingredients_list = ["flour", "milk", "eggs", "hello", "no", "chicken", "salt", "pepper"]
units_list = ["cup", "tsp", "", "lb", "tbsp", "g", "g", "g"]
amount_list = [2, 3, 4, 5, 6, 500, 10, 5]
converted_units_list = []
converted_amount_list = [1, 5, 10, 0.2]
ml_list = {
    "mL": 1,
    "L": 1000,
    "quart": 946,
    "pint": 473,
    "cup": 250,
    "tbsp": 15,
    "tsp": 5
}
g_list = {
    "g": 1,
    "lb": 454,
    "stick": 113,
    "oz": 28.35
}
count = 0
finished_amount_list = [] '''


''' def string_check(question, answer):
    valid = False

    while not valid:
        response = input(question).lower()

        if response in answer:
            return response

        else:
            for thing in answer:
                if response == thing[0]:
                    return thing

            print("Error: Please answer with yes or no")


converted_recipe = []
method = ()
want_method = string_check("Would you like to add a method to your new recipe? ", ["yes", "no"])

if want_method == "yes":
    method = input("Enter here: ")

else:
    pass

if method != ():
    converted_recipe.append(method)

print(converted_recipe) '''


''' def num_check(question):
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


ingredients_list = ["flour", "eggs", "milk"]
amount_list = []

for item in ingredients_list:
    amount = num_check("Amount of " + item + ": ")
    amount_list.append(amount)
print(amount_list) '''


''' def ingredient_check(question):
    valid = False
    while not valid:
        item = input(question)
        number_regex = "^[0.01-100000]"
        try:
            amount = float(item[0])
        except ValueError:
            print("Error: Please enter an amount")

        for word in item:
            if word in valid_unit_list:
                if len(item) >= 3:
                    if word.index == 2:
                        continue

        unit = item[1]
        ingredient_name = item[2:]

        if re.match(number_regex, item):
            pass
        else:
            continue

        if amount < 0.01:
            print("Error: Amount is too small, consider using a different unit")

        elif amount > 100000:
            print("Error: Amount is too large, consider using a different unit")

        else:
            print("Error")

        if unit not in valid_unit_list:
            print("Error: Please enter a valid unit")
        else:
            connect = [amount, unit, ingredient_name]
            join = " ".join(connect)
            return join '''


''' valid_unit_list = [
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

ingredient_list = []
keep_going = False
while not keep_going:
    ingredient_list.append(ingredient_check("Enter an ingredient: "))
    print(ingredient_list)


def num_check(question):
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


def unit_check(question):
    valid = False

    while not valid:
        response = input(question).lower()

        for var_list in valid_unit_list:
            if response in var_list:
                response = var_list[0]
                return response

        else:
            print("Error: Please enter a valid unit")


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("Error: Name cannot be blank")


def string_check(question, answer):
    valid = False

    while not valid:
        response = input(question).lower()

        if response in answer:
            return response

        else:
            for thing in answer:
                if response == thing[0]:
                    return thing

            print("Error: Please answer with yes or no")


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
count = 0
keep_going = ()
ingredients_list = []

while keep_going != "no":
    amount = num_check("Amount: ")
    unit = unit_check("Unit: ")

    complete = False
    while not complete:
        ingredient_name = not_blank("Enter an ingredient: ")
        ingredients_list.append(ingredient_name)
        count += 1
        keep_going = string_check("Enter more ingredients? ", ["yes", "no"])
        complete = True

        if keep_going == "yes" and count >= 2:
            complete = True
            print()

        elif keep_going == "yes" and count < 2:
            print("Error: Please enter at least 2 ingredients")

        else:
            break '''


''' valid_unit_list = [
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
ml_list = {
    "mL": 1,
    "L": 1000,
    "quart": 946,
    "pint": 473,
    "cup": 250,
    "tbsp": 15,
    "tsp": 5
}
g_list = {
    "g": 1,
    "mg": 0.001,
    "kg": 1000,
    "lb": 454,
    "stick": 113,
    "oz": 28.35
}
exit_code = "xxx"
ingredients_list = ["flour", "milk", "eggs", "hello", "no", "chicken", "salt", "pepper"]
units_list = ["cup", "tsp", "", "lb", "tbsp", "g", "g", "g"]
plural_list = []
amount_list = [2, 3, 4, 5, 6, 500, 10, 5]
converted_units_list = []
converted_amount_list = []
finished_amount_list = []
converted_recipe = []


def convert_grams(obj):
    valid = False

    while not valid:
        with open("conversions.csv", mode="r") as csvfile:
            conversions_sheet = csv.DictReader(csvfile)

            if obj in ml_list:
                conversion = amount_list[ind] * ml_list[obj]
                divide = conversion / 250

                try:
                    for row in conversions_sheet:
                        if ingredients_list[ind] == row["Ingredients"]:
                            conversion = divide * float(row["grams per 250ml"])
                            converted_units_list.append("g")
                            return conversion

                finally:
                    if ingredients_list[ind] != row["Ingredients"]:
                        converted_units_list.append("mL")
                        return conversion

            if obj in g_list:
                conversion = amount_list[ind] * g_list[obj]
                converted_units_list.append("g")
                return conversion

            if obj == "":
                converted_units_list.append("")
                return amount_list[ind]


ind = 0
for item in units_list:
    converted_amount_list.append(convert_grams(item))
    ind += 1

print(converted_amount_list)
print(converted_units_list) '''


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("Error: Name cannot be blank")


def unit_check(question):
    valid = False

    while not valid:
        response = input(question).lower()

        for var_list in valid_unit_list:
            if response in var_list:
                response = var_list[0]
                try:
                    plural_list.append(var_list[1])
                except IndexError:
                    plural_list.append("")
                return response

        else:
            print("Error: Please enter a valid unit")


def num_check(question):
    valid = False

    while not valid:
        response = input(question)

        try:
            if float(response) <= 0:
                print("Error: Number cannot be 0 or less")

            if float(response) < 0.01:
                print("Error: Number is too small")

            else:
                return response

        except ValueError:
            print("Error: Please enter a number")


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
exit_code = "xxx"
ingredients_list = []
units_list = []
amount_list =[]
plural_list = []
count = 0
complete = False

while not complete:
    ingredient_name = not_blank("Enter an ingredient: ")

    if ingredient_name == exit_code and count >= 2:
        complete = True
        print("\nHere is your list of ingredients:")
        print(ingredients_list)
        print(units_list)
        print(amount_list)

    elif ingredient_name == exit_code and count < 2:
        print("Error: Please enter at least 2 ingredients")

    else:
        ingredients_list.append(ingredient_name)
        unit_name = unit_check("Unit of " + ingredient_name + ": ")
        units_list.append(unit_name)
        if plural_list[count] == "":
            amount = num_check("Amount of " + ingredient_name + ": ")
        else:
            amount = num_check("Amount (in " + plural_list[count] + ") of " + ingredient_name + ": ")
        amount_list.append(float(amount))
        count += 1
        print("Accepted. Continue to enter more ingredients or type 'xxx' when done.")

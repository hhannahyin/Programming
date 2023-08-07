# Import Statements
import csv
import os
import sys


# ------ Functions ------

# Function for checking string input is a valid answer (yes or no)
def string_check(question, answer):
    valid = False

    while not valid:
        response = input(question).lower()

        if response == "r":
            print("===================================================================================================="
                  "===========")
            print("Restarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        if response in answer:
            return response

        else:
            for thing in answer:
                if response == thing[0]:
                    return thing

            print("Error: Please answer with yes or no\n")


# Function for checking for blank inputs
def not_blank(question):
    valid = False

    while not valid:
        response = input(question).lower()

        if response == "r":
            print("===================================================================================================="
                  "===========")
            print("Restarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        if response != "":
            return response

        else:
            print("Error: Name cannot be blank\n")


# Function for checking for number inputs above 0
def num_check(question):
    valid = False

    while not valid:
        response = input(question).lower()

        if response == "r":
            print("===================================================================================================="
                  "===========")
            print("Restarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        try:
            if float(response) <= 0:
                print("Error: Number cannot be 0 or less\n")

            if 0 < float(response) < 0.01:
                print("Error: Number is too small\n")

            else:
                return response

        except ValueError:
            print("Error: Please enter a number\n")


# Function for checking input is in the list of valid units
def unit_check(question):
    valid = False

    while not valid:
        response = input(question).lower()

        if response == "r":
            print("===================================================================================================="
                  "===========")
            print("Restarting...")
            os.execl(sys.executable, sys.executable, *sys.argv)

        for var_list in valid_unit_list:
            if response in var_list:
                response = var_list[0]
                try:
                    plural_list.append(var_list[1])
                except IndexError:
                    plural_list.append("")
                return response

        else:
            print("Error: Please enter a valid unit\n")


# Function for converting ingredients to grams
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


# Function for removing '.0'
def format_num(num):
    if num % 1 == 0:
        return int(num)

    else:
        return num


# ------ Main Routine ------

# Dictionaries/Lists
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
ingredients_list = []
units_list = []
plural_list = []
amount_list = []
converted_units_list = []
converted_amount_list = []
finished_amount_list = []
converted_recipe = []

# Opening Message
print("===============================================================================================================")
print("Welcome to the Recipe Converter!")
print("Press r at anytime to restart the program\n")
# Instructions
used_before = string_check("Have you used this program before? If you have but would like to review the instructions, "
                           "also enter no.\nEnter here (yes/no): ", ["yes", "no"])

if used_before == "no":
    print("========================================== INSTRUCTIONS ===================================================")
    print("This program will help you to develop a delicious recipe from ingredients that you may have available in "
          "your pantry.\nWhat it does is converts your ingredients into grams, and then resizes them to your liking.")
    print("\nWhen prompted, in this order, please enter:"
          "\n   1. The name of your recipe, "
          "\n   2. The names of each ingredients, "
          "\n   3. The unit of measurement of each ingredient, "
          "\n   4. The amount of each ingredient, "
          "\n   5. The serving size of your recipe and your desired size, "
          "\n   6. (Optional) Instructions on how to make your recipe. ")
    print("\nThe program will write a new and improved recipe for you to enjoy! ")

else:
    print("============================================================================================================"
          "===")
    print("Thank you for your continued support towards this program!")

# Recipe Name
print("===============================================================================================================")
print("Now, please enter the name of your recipe.")
recipe_name = not_blank("Recipe Name: ")
print()
print("===============================================================================================================")

# Ingredient Name Collection
print("Please enter the names of the ingredients in your recipe. \nDo not include the units or amounts, just the name. "
      "\nPlease type 'xxx' when you have finished submitting ingredients. ")

count = 0
complete = False

while not complete:
    ingredient_name = not_blank("Enter an ingredient: ")

    if ingredient_name == exit_code and count >= 2:
        complete = True
        print("\nHere is your list of ingredients:")
        print(ingredients_list)
        print("\n======================================================================================================"
              "=========")

    elif ingredient_name == exit_code and count < 2:
        print("Error: Please enter at least 2 ingredients\n")

    else:
        print("Accepted. Continue to enter more ingredients or type 'xxx' when done.\n")
        count += 1
        ingredients_list.append(ingredient_name)

# Unit Collection
print("Now please enter in the unit that each ingredient in measured in, e.g. grams, kilograms, cups.")
print("Do not yet enter the amount, only include the unit that the ingredient is measured in in your answer.")

for item in ingredients_list:
    unit_name = unit_check("Unit of " + item + ": ")
    print("Accepted!\n")
    units_list.append(unit_name)

# Amount Collection
print("===============================================================================================================")
print("And next please enter the amount of each ingredient needed, e.g if the recipe calls for 500 grams of chicken, "
      "type '500'")
count = 0
for item in ingredients_list:

    if plural_list[count] == "":
        amount = num_check("Amount of " + item + ": ")

    else:
        amount = num_check("Amount (in " + plural_list[count] + ") of " + item + ": ")
    print("Accepted!\n")
    amount_list.append(float(amount))
    count += 1

# Serving Size
print("===============================================================================================================")
print("What is the serving size of this recipe? (Serving size is how many people the current recipe serves)")
serving_size = float(num_check("Serving size: "))

# Servings Desired
print("\nWhat is your desired serving size? (Desired size is how many people you want the new recipe to serve)")
desired_size = ()
keep_going = True
while keep_going:
    desired_size = float(num_check("Desired size: "))
    if desired_size / serving_size >= 0.01:
        keep_going = False
    else:
        print("Error: Your recipe will be too small. Because of your large serving size, your desired size should be at"
              " least " + str(format_num(serving_size * 0.01)) + "\n")

# Scale Factor
scale_factor = round(desired_size / serving_size, 2)
print("The scale factor of your new recipe compared to the original is: " + str(scale_factor))

# Convert Ingredients to Grams
ind = 0
for item in units_list:
    converted_amount_list.append(convert_grams(item))
    ind += 1

# Scale Ingredients
for item in converted_amount_list:
    scale = item * scale_factor
    ind = converted_amount_list.index(item)

    if converted_units_list[ind] == "mg":
        if scale >= 1000:
            scale = scale / 1000
            converted_units_list[ind] = "g"

    if converted_units_list[ind] == "g":
        if scale < 1:
            scale = scale * 1000
            converted_units_list[ind] = "mg"

        if scale >= 1000:
            scale = scale / 1000
            converted_units_list[ind] = "kg"

    if converted_units_list[ind] == "kg":
        if scale < 1:
            scale = scale * 1000
            converted_units_list[ind] = "g"

    if converted_units_list[ind] == "mL":
        if scale >= 1000:
            scale = scale / 1000
            converted_units_list[ind] = "L"

    if converted_units_list[ind] == "L":
        if scale < 1:
            scale = scale * 1000
            converted_units_list[ind] = "mL"

    if scale < 0.01:
        finished_amount_list.append(scale)
    else:
        finished_amount_list.append(format_num(round(scale, 2)))

# Method
print()
print("===============================================================================================================")
method = ()
want_method = string_check("Would you like to add a method to your new recipe? (Instructions on how to make your "
                           "recipe)\nEnter here (yes/no): ", ["yes", "no"])

if want_method == "yes":
    print("\nPlease enter your method now. You may enter as many lines of text as you want. When you're done, enter the"
          " exit code 'xxx' on a line by itself.")
    buffer = []
    while True:
        line = input("Enter here: ")
        if line == exit_code:
            break
        buffer.append(line)
    method = "\n".join(buffer)

else:
    pass

# New Ingredient List
print()
print("===============================================================================================================")
print("Creating your new recipe...")
print("===============================================================================================================")
print(recipe_name.title() + "\n\nIngredients:")

count = 0
while count != len(ingredients_list):
    converted_recipe.append(str(finished_amount_list[count]) + converted_units_list[count] + " " +
                            ingredients_list[count])
    count += 1

if method != ():
    converted_recipe.append("\n" + method)

finished_list = "\n".join(converted_recipe)
print(finished_list)
print()

# Final Message and Option to Restart
print("===============================================================================================================")
print("Thank you for using my program!")
restart = input("Press r if you would like to try again\n")
if restart.lower() == "r":
    os.execl(sys.executable, sys.executable, *sys.argv)
else:
    print("\nGoodbye!")

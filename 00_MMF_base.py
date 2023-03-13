# import statements

# ------ functions ------

# checks that the name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # if the name is not blank, then the program continues
        if response != "":
            return response

        # if the name is blank, then an error message is printed and the loop is repeated
        else:
            print("Error: Name cannot be blank")


# checks that the value entered is a number that is more than 0
def int_check(question):
    valid = False

    while not valid:
        response = input(question)

        try:
            # error message is printed if the number is equal to or less than 0, loop repeats
            if float(response) <= 0:
                print("Error: Number must be more than 0")

            # if the value meets the criteria, program continues
            else:
                return response

        # if the value entered cannot be turned into a float, then an error message is printed and the loop repeats
        except ValueError:
            print("Error: Please enter a number")


# checks that the unit entered is valid
def unit_check(question):
    # list of units that the user is allowed to enter
    valid_unit_list = ["", "g", "mg", "kg", "ml", "L", "tsp", "Tbsp", "cup", "cups", "oz", "pint", "pints", "quart",
                       "quarts", "lb", "stick", "sticks"]
    valid = False

    while not valid:
        response = input(question)

        # prints an error message when the unit that the user typed is not one of the units in the valid list
        if response not in valid_unit_list:
            print("Error: Please enter a valid unit")
        # program continues when a valid unit is entered
        else:
            return response


# ------ Main Routine ------

# dictionaries / lists to hold data
exit_code = "xxx"
ingredients_list = []
units_list = []
amount_list = []
count = 0

# get recipe name
recipe_name = not_blank("Recipe Name: ")

# instructions for inputting ingredient names
print("Please enter the names of the ingredients in your recipe. \nDo not include the units or measurements, "
      "just the name. \nPlease type 'xxx' when you have finished submitting ingredients. ")

ok = False

# loop to ask for recipe ingredients
while not ok:
    ingredient_name = input("Enter an ingredient: ")

    # prints an error message if the name is blank
    if ingredient_name == "":
        print("Error: Name cannot be blank")

    # prints an error message if user tries to end the loop but hasn't met the requirements yet
    elif ingredient_name == exit_code and count < 2:
        print("Error: Please enter at least 2 ingredients")

    # ends the loops and prints the list of ingredients
    elif ingredient_name == exit_code and count >= 2:
        ok = True
        print("Here is your list of ingredients:")
        print(ingredients_list)

    # adds an ingredient to the list
    else:
        ingredients_list.append(ingredient_name)
        count += 1

# gets the unit of measurement for every ingredient entered previously
for item in ingredients_list:
    unit_name = unit_check("Unit of " + item + ": ")
    units_list.append(unit_name)

# gets the amount needed for every ingredient entered previously
for item in ingredients_list:
    amount = int_check("Amount of " + item + ": ")
    amount_list.append(amount)

# get recipe serving size
serving_size = float(int_check("What is the serving size of this recipe? "))

# ask for servings desired
desired_size = float(int_check("What is your desired serving size? "))

# find scale factor
scale_factor = round(desired_size / serving_size, 2)

print("The scale factor is: " + str(scale_factor))

# convert relevant ingredients to grams

# scale ingredients

# output new, updated ingredient list

# import statements

import csv
with open("/Users/hannah/Downloads/Conversions - Sheet1.csv", mode="r") as csvfile:
    conversions_sheet = csv.DictReader(csvfile)


# ------ functions ------

# checks that the response entered is yes or no
def string_check(question, answer):

    valid = False

    while not valid:
        response = input(question).lower()

        # if the response is yes or no, then the answer is accepted and the program continues
        if response in answer:
            return response

        else:
            # checks if the user possibly entered 'y' or 'n' for short of yes/no and accepts that answer too
            for thing in answer:
                if response == thing[0]:
                    return thing

            # prints an error message if the answer is not yes or no
            print("Error: Please answer with yes or no")


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
instructions = "This program will help you to convert your recipes to grams and resize them to your liking. When \n" \
               "prompted, please enter individually the name of your recipe, the names of the ingredients, the unit\n" \
               "and amount of which these ingredients are measured in, and the serving size of your recipe. Then \n" \
               "the program will write a new and improved recipe for you to enjoy! :)\n"
exit_code = "xxx"
ingredients_list = []
units_list = []
amount_list = []
converted_list = []
count = 0

# prints instructions for user if they've never used this program before
used_before = string_check("Have you used this program before? ", ["yes", "no"])

if used_before == "no":
    print(instructions)

else:
    print("OK! Thank you for your continued support towards this program :)\n")

# get recipe name
print("Please enter the name of your recipe")
recipe_name = not_blank("Recipe Name: ")

# instructions for inputting ingredient names
print("\nPlease enter the names of the ingredients in your recipe. \nDo not include the units or measurements, "
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
    amount_list.append(float(amount))

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
print(recipe_name.title() + "\n\nIngredients:")

count = 0
done = False

while done is False:

    if count != len(ingredients_list):
        converted_list.append(str(amount_list[count]) + " " + units_list[count] + " " + ingredients_list[count])
        count += 1

    else:
        done = True
        finished_list = "\n".join(converted_list)
        print(finished_list)

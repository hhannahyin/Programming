# import statements

# functions go here

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
                print("Error: Serving size must be more than 0")

            # if the value meets the criteria, program continues
            else:
                return response

        # if the value entered cannot be turned into a float, then an error message is printed and the loop repeats
        except ValueError:
            print("Error: Please enter a number")


# ------Main Routine------


# dictionaries / lists needed to hold data
ingredients_list = []
exit_code = "xxx"
count = 0

# get recipe name
recipe_name = not_blank("Recipe Name: ")

# loop to get recipe ingredients (end when exit code is typed)

# get ingredient name

# get unit of measurement

# get amount

# store item as a unit (use list)

# when exit code is typed check that the recipe has at least 2 ingredients and end collection loop

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

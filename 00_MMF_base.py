# import statements

# functions go here

# checks that the recipe name is not blank
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

# Main Routine


# Set up dictionaries / lists needed to hold data

# Get recipe name

recipe_name = not_blank("Recipe Name: ")

# Loop to get recipe ingredients (end when exit code is typed)

# Get ingredient name

# Get unit of measurement

# Get amount

# Store item as a unit (use list)

# When exit code is typed check that the recipe has at least 2 ingredients and end collection loop

# Get recipe serving size

# Ask for servings desired

# Find scale factor

# Convert relevant ingredients to grams

# Scale ingredients

# Output new, updated ingredient list

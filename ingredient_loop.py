ingredients_list = []
exit_code = "xxx"
count = 0

print("Please enter the names of the ingredients in your recipe. \nDo not include the units or measurements, "
      "just the name. \nPlease type 'xxx' when you have finished submitting ingredients. ")

valid = False

while not valid:
    ingredient_name = input("Enter an ingredient: ")

    if ingredient_name == "":
        print("Error: Name cannot be blank")

    elif ingredient_name != exit_code:
        ingredients_list.append(ingredient_name)
        count += 1

    elif ingredient_name == exit_code and count >= 2:
        valid = True
        print("Here is your list of ingredients:")
        print(ingredients_list)

    elif ingredient_name == exit_code and count < 2:
        print("Error: Please enter at least 2 ingredients")

ingredients_list = []
exit_code = "xxx"
count = 0
valid = True

print("Please enter the names of the ingredients in your recipe. \nDo not include the units or measurements, "
      "just the name. \nPlease type 'xxx' when you have finished submitting ingredients. ")

while valid:
    ingredient_name = input("Enter an ingredient: ")

    if ingredient_name != exit_code:
        ingredients_list.append(ingredient_name)
        count += 1

    if ingredient_name == exit_code and count >= 2:
        valid = False
        print("Here is your list of ingredients:")
        print(ingredients_list)

    if ingredient_name == exit_code and count < 2:
        print("Error: Please enter at least 2 ingredients")

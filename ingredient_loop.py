ingredients_list = []
exit_code = "xxx"
count = 0

valid = True
while valid:
    ingredient_name = input("Enter an ingredient: ")

    if ingredient_name != exit_code:
        ingredients_list.append(ingredient_name)
        count += 1

    if ingredient_name == exit_code and count >= 2:
        valid = False
        print(ingredients_list)

    if ingredient_name == exit_code and count < 2:
        print("Error")


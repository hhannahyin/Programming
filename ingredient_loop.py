ingredients_list = []
exit_code = "xxx"
count = 0

valid = True
while valid:
    ingredients_list.append(input("Enter an ingredient: "))

    if ingredients_list[-1] != exit_code:
        count += 1

    if ingredients_list[-1] == exit_code and count >= 2:
        valid = False
        print(ingredients_list)

    if ingredients_list[-1] == exit_code and count <= 2:
        print("Error")


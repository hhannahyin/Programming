def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Error: Name cannot be blank")


recipe_name = not_blank("Recipe Name: ")

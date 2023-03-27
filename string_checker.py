def string_check(question, answer):

    valid = False

    while not valid:
        response = input(question).lower()

        if response in answer:
            return response

        else:
            for item in answer:
                if response == item[0]:
                    return item

            print("Error: Please answer with yes or no")


instructions = "This program will help you to convert your recipes to grams and resize them to your liking. When \n" \
               "prompted, please enter individually the name of your recipe, the names of the ingredients, the unit\n" \
               "and amount of which these ingredients are measured in, and the serving size of your recipe. Then \n" \
               "the program will write a new and improved recipe for you to enjoy! :)\n"

used_before = string_check("Have you used this program before? ", ["yes", "no"])

if used_before == "no":
    print(instructions)

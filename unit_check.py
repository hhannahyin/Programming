def unit_check(question):
    valid_unit_list = ["", "g", "mg", "kg", "ml", "L", "tsp", "Tbsp", "cup", "cups", "oz", "pint", "pints", "quart",
                       "quarts", "lb", "stick", "sticks"]
    valid = False

    while not valid:
        response = input(question)

        if response not in valid_unit_list:
            print("Error: Please enter a valid unit")
        else:
            return response


unit_name = unit_check("Unit: ")

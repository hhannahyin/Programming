def int_check(question):
    valid = False

    while not valid:
        response = input(question)

        try:
            if float(response) <= 0:
                print("Error: Number must be more than 0")

            else:
                return response

        except ValueError:
            print("Error: Please enter a number")


serving_size = float(int_check("What is the serving size of this recipe? "))
desired_size = float(int_check("What is your desired serving size? "))

scale_factor = round(desired_size / serving_size, 2)

print("The scale factor is: " + str(scale_factor))

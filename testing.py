import csv

ingredients_list = ["flour", "milk", "eggs", "hello", "no", "chicken", "salt", "pepper"]
units_list = ["cup", "tsp", "", "lb", "tbsp", "g", "g", "g"]
amount_list = [2, 3, 4, 5, 6, 500, 10, 5]
converted_units_list = []
converted_amount_list = []
ml_list = {
    "mL": 1,
    "L": 1000,
    "quart": 946,
    "pint": 473,
    "cup": 250,
    "tbsp": 15,
    "tsp": 5
}
g_list = {
    "g": 1,
    "lb": 454,
    "stick": 113,
    "oz": 28.35
}
count = 0


# conversions
def conversion_check(item):
    valid = False

    while not valid:
        with open("/Users/hannah/Downloads/conversions.csv", mode="r") as csvfile:
            conversions_sheet = csv.DictReader(csvfile)

            if item in ml_list:
                convert = amount_list[count] * ml_list[item]
                divide = convert / 250

                try:
                    for row in conversions_sheet:
                        if ingredients_list[count] == row["Ingredients"]:
                            convert = divide * float(row["grams per 250ml"])
                            converted_units_list.append("g")
                            return convert
                finally:
                    if ingredients_list[count] != row["Ingredients"]:
                        converted_units_list.append("mL")
                        return convert

            if item in g_list:
                convert = amount_list[count] * g_list[item]
                converted_units_list.append("g")
                return convert

            if item == "":
                converted_units_list.append("")
                return amount_list[count]


for x in units_list:
    converted_amount_list.append(conversion_check(x))
    count += 1

print(converted_amount_list)
print(converted_units_list)


''' for item in units_list:

    if item in ml_list:
        convert = amount_list[count] * ml_list[item]
        divide = convert / 250
        count += 1
        print(convert, divide)

        with open("/Users/hannah/Downloads/conversions.csv", mode="r") as csvfile:
            conversions_sheet = csv.DictReader(csvfile)
            for x in ingredients_list:
                for row in conversions_sheet:
                    if x == row["Ingredients"]:

                        if float(row["grams per 250ml"]) in previous:
                            break

                        else:
                            print(row["grams per 250ml"])
                            conversion = divide * float(row["grams per 250ml"])
                            converted_amount_list.append(round(conversion, 2))
                            converted_units_list.append("g")
                            previous.append(conversion / divide)
                            print(previous)
                            print(conversion)

    if item in g_list:
        convert = amount_list[count] * g_list[item]
        count += 1
        print(convert)
        converted_amount_list.append(convert)
        converted_units_list.append("g")

    if item == "":
        ind = units_list.index(item)
        converted_amount_list.append(amount_list[ind])
        converted_units_list.append("")


print(converted_amount_list)
print(converted_units_list) '''

# ingredient collection function
''' ingredients_list = []
answer = ()
count = 0


def ingredient_loop(question, exit_code):
    valid = False

    while not valid:
        ingredient_name = input(question)

        if ingredient_name == exit_code and count >= 2:
            print(ingredients_list)
            break

        elif ingredient_name == exit_code and count < 2:
            print("Error: Please enter at least 2 ingredients")

        else:
            count += 1
            return ingredient_name


while answer != exit_code:
    answer = ingredient_loop("Enter an ingredient: ", "xxx")
    count += 1
    ingredients_list.append(answer) '''

# regular ingredient collection (done)
''' def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response

        else:
            print("Error: Name cannot be blank")


ingredients_list = []
exit_code = "xxx"
count = 0

complete = False

while not complete:
    ingredient_name = not_blank("Enter an ingredient: ")

    if ingredient_name == exit_code and count >= 2:
        complete = True
        print(ingredients_list)

    elif ingredient_name == exit_code and count < 2:
        print("Error: Please enter at least 2 ingredients")

    else:
        count += 1
        ingredients_list.append(ingredient_name) '''

# units for testing
''' ingredients_list = ["milk", "sugar", "eggs"]
converted_units_list = ["mL", "g", ""]
finished_amount_list = [250, 100, 2]
converted_recipe = []
recipe_name = "cheesy pasta"
count = 0

print(recipe_name.title() + "\n\nIngredients:")

while count != len(ingredients_list):
    converted_recipe.append(str(finished_amount_list[count]) + converted_units_list[count] + " " +
                            ingredients_list[count])
    count += 1

finished_list = "\n".join(converted_recipe)
print(finished_list) '''

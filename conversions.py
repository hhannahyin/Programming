import csv


def conversion_check(item):

    valid = False

    while not valid:
        with open("/Users/hannah/Downloads/conversions.csv", mode="r") as csvfile:
            conversions_sheet = csv.DictReader(csvfile)

            if item in ml_list:
                convert = amount_list[ind] * ml_list[item]
                divide = convert / 250
                print(convert, divide)

                try:
                    for row in conversions_sheet:
                        if ingredients_list[ind] == row["Ingredients"]:
                            print(row["grams per 250ml"])
                            convert = round(divide * float(row["grams per 250ml"]), 2)
                            converted_units_list.append("g")
                            print(convert)
                            return convert

                finally:
                    if ingredients_list[ind] != row["Ingredients"]:
                        converted_units_list.append("mL")
                        return convert

            if item in g_list:
                print(amount_list[ind])
                convert = amount_list[ind] * g_list[item]
                print(convert)
                converted_units_list.append("g")
                return convert

            if item == "":
                convert = amount_list[ind]
                converted_units_list.append("")
                return convert


ingredients_list = ["flour", "milk", "eggs", "hello", "no", "chicken", "salt", "pepper"]
units_list = ["cup", "tsp", "", "lb", "tbsp", "g", "g", "g"]
amount_list = [2, 3, 4, 5, 6, 500, 10, 5]
converted_units_list = []
converted_amount_list = []
ind_list = []
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


for y in units_list:
    ind = units_list.index(y)

    if ind not in ind_list:
        pass

    else:
        while ind in ind_list:
            ind += 1

    ind_list.append(ind)
    print(ind)
    print(ind_list)
    converted = conversion_check(y)
    converted_amount_list.append(converted)

print(converted_amount_list)
print(converted_units_list)

import csv
with open("/Users/hannah/Downloads/conversions.csv", mode="r") as csvfile:
    conversions_sheet = csv.DictReader(csvfile)

ingredients_list = ["flour", "milk", "eggs", "hello"]
units_list = ["cup", "tsp", "", "lb"]
amount_list = [2, 3, 4, 5]
previous = []
converted_units_list = []
converted_amount_list = []
count = 0

valid_units_list = [
    [""],
    ["g", "grams", "gram"],
    ["mg", "milligrams", "milligram"],
    ["kg", "kilograms", "kilogram"],
    ["mL", "millilitres", "ml", "mls", "millilitre"],
    ["L", "litres", "l", "litre"],
    ["quart", "quarts", "fl qt", "qt", "q"],
    ["pint", "pints", "fl pt", "pt", "p"],
    ["cup", "cups", "c"],
    ["tbsp", "tablespoons", "tablespoon", "tbs"],
    ["tsp", "teaspoons", "teaspoon"],
    ["lb", "pounds", "lbs", "pound"],
    ["stick", "sticks"],
    ["oz", "ounces", "ounce", "fl oz", "fluid ounces", "fluid ounce"]
]


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


for item in units_list:

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
print(converted_units_list)

''' else:
ind = units_list.index(item)
if len(converted_amount_list) > 0:
    if converted_amount_list[-1] != amount_list[ind]:
        converted_amount_list.append(amount_list[ind])
break '''
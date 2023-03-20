import csv
with open("/Users/hannah/Downloads/Conversions - Sheet1.csv", mode="r") as csvfile:
    conversions_sheet = csv.DictReader(csvfile)

ingredients_list = []
units_list = []
amount_list = []

converted_amount_list = []

valid_units_list = [
    [""],
    ["gram", "grams", "g"],
    ["milligram", "milligrams", "mg"],
    ["kilogram", "kilograms", "kg"],
    ["millilitre", "millilitres", "ml", "mls", "mL", "mLs"],
    ["litre", "L", "l"],
    ["quart", "quarts", "q"],
    ["pint", "pints", "p"],
    ["cup", "cups", "c"],
    ["tbsp", "Tbsp", "tablespoon", "tablespoons", "T"],
    ["tsp", "teaspoon", "teaspoons", "t"],
    ["pound", "pounds", "p", "lb", "lbs"],
    ["stick", "sticks"],
    ["ounce", "ounces", "oz", "fl oz"]
]


ml_list = {
    "millilitre": 1,
    "quart": 946,
    "pint": 473,
    "cup": 250,
    "tbsp": 15,
    "tsp": 5
}

g_list = {
    "gram": 1,
    "pound": 454,
    "stick": 113,
    "ounce": 28.35
}

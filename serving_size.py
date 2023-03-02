serving_size = ()

while serving_size == ():

    try:
        serving_size = float(input("What is the serving size for this recipe? "))

    except ValueError:
        print("Error: Please enter a number")

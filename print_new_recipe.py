ingredients_list = ["flour", "eggs"]
units_list = ["cups", ""]
amount_list = [2, 2]

converted_list = []
second_count = 0

done = False

while done is False:

    if second_count != len(ingredients_list):
        converted_list.append(str(amount_list[second_count]) + " " + units_list[second_count] + " " + ingredients_list
                              [second_count])
        second_count += 1

    else:
        done = True
        finished_list = "\n".join(converted_list)
        print(finished_list)

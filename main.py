def read_txt(file_name, encoding="utf-8"):
    cook_recipe = []
    with open(file_name) as file:
        #print(type(file))
        for line in file:
            cook_recipe.append(line.strip())
            number_recipe = int(file.readline().strip())
            for line_ingredients in range(number_recipe):
                print(file.readline())
            file.readline()

    #print(cook_recipe)

read_txt('recipes.txt')